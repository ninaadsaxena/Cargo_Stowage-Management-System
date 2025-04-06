from fastapi import APIRouter
from schemas import SimulationRequest, SimulationResponse
from datetime import datetime, timedelta
from crud import query_db, execute_db, get_item_by_id, update_item

router = APIRouter()

@router.post("/day")
async def simulate_day(request: SimulationRequest):
    new_date = (datetime.strptime(currentDate, "%Y-%m-%d") + timedelta(days=request.numOfDays or 1)).strftime("%Y-%m-%d")
    items_used = []
    items_expired = []
    items_depleted_today = []

    for usage_item in request.itemsToBeUsedPerDay:
        item = get_item_by_id(usage_item.itemId or usage_item.name)
        if item and not item.isWaste:
            item.usageCount += 1
            if item.usageCount >= item.usageLimit:
                item.isWaste = True
                items_depleted_today.append({"itemId": item.itemId, "name": item.name})
            items_used.append({"itemId": item.itemId, "name": item.name, "remainingUses": item.usageLimit - item.usageCount if item.usageLimit else None})
            update_item(item.itemId, item)

    expired_items = query_db('SELECT * FROM items WHERE expiryDate <= ?', [new_date])
    for item in expired_items:
        item.isWaste = True
        items_expired.append({"itemId": item["id"], "name": item["name"]})
        update_item(item["id"], item)

    execute_db('UPDATE current_date SET date = ?', [new_date])

    return SimulationResponse(success=True, newDate=new_date, changes={"itemsUsed": items_used, "itemsExpired": items_expired, "itemsDepletedToday": items_depleted_today})
