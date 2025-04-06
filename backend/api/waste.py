from fastapi import APIRouter
from schemas import WasteIdentificationResponse, WasteReturnPlanRequest, WasteReturnPlanResponse
from crud import get_item_by_id, create_log, get_container_by_id, update_container

router = APIRouter()

@router.get("/identify")
async def identify_waste():
    waste_items = query_db('SELECT * FROM items WHERE isWaste = 1 OR expiryDate <= ? OR usageCount >= usageLimit', [currentDate])
    formatted_waste = []
    for item in waste_items:
        reason = "Expired" if item["expiryDate"] <= currentDate else "Out of Uses" if item["usageCount"] >= item["usageLimit"] else "Manually Marked"
        formatted_waste.append({
            "itemId": item["id"],
            "name": item["name"],
            "reason": reason,
            "containerId": item["containerId"],
            "position": {
                "startCoordinates": {"width": item["x"], "depth": item["y"], "height": item["z"]},
                "endCoordinates": {"width": item["x"] + item["width"], "depth": item["y"] + item["depth"], "height": item["z"] + item["height"]}
            }
        })
    return WasteIdentificationResponse(success=True, wasteItems=formatted_waste)

@router.post("/return-plan")
async def waste_return_plan(request: WasteReturnPlanRequest):
    container = get_container_by_id(request.undockingContainerId)
    if not container:
        raise HTTPException(status_code=404, detail="Container not found")

    waste_items = query_db('SELECT * FROM items WHERE isWaste = 1 OR expiryDate <= ? OR usageCount >= usageLimit', [request.undockingDate])
    waste_items.sort(key=lambda x: x["mass"])
    selected_items = []
    total_weight = 0
    for item in waste_items:
        if total_weight + item["mass"] <= request.maxWeight:
            selected_items.append(item)
            total_weight += item["mass"]

    return_plan = []
    step = 1
    for item in selected_items:
        return_plan.append({
            "step": step,
            "itemId": item["id"],
            "itemName": item["name"],
            "fromContainer": item["containerId"],
            "toContainer": request.undockingContainerId
        })
        step += 1

    retrieval_steps = []
    for item in selected_items:
        container = get_container_by_id(item["containerId"])
        if container:
            steps = calculate_retrieval_steps(item, container)
            retrieval_steps.extend(steps)

    return_manifest = {
        "undockingContainerId": request.undockingContainerId,
        "undockingDate": request.undockingDate,
        "returnItems": [{"itemId": item["id"], "name": item["name"], "reason": "Expired" if item["expiryDate"] <= request.undockingDate else "Out of Uses"} for item in selected_items],
        "totalVolume": sum(item["width"] * item["depth"] * item["height"] for item in selected_items),
        "totalWeight": total_weight
    }

    return WasteReturnPlanResponse(success=True, returnPlan=return_plan, retrievalSteps=retrieval_steps, returnManifest=return_manifest)

def calculate_retrieval_steps(item, container):
    return [{"step": 1, "action": "retrieve", "itemId": item["id"], "itemName": item["name"]}]
