from fastapi import APIRouter, HTTPException
from typing import Optional
from schemas import ItemSearchResponse, RetrievalRequest
from crud import get_item_by_id, create_log, query_db

router = APIRouter()

@router.get("/search")
async def item_search(itemId: Optional[str] = None, itemName: Optional[str] = None, userId: Optional[str] = None):
    if itemId:
        item = get_item_by_id(itemId)
    elif itemName:
        item = query_db('SELECT * FROM items WHERE name LIKE ?', [f'%{itemName}%'], one=True)
    else:
        raise HTTPException(status_code=400, detail="Either itemId or itemName must be provided")

    if not item:
        return ItemSearchResponse(success=True, found=False, item=None, retrievalSteps=[])

    retrieval_steps = calculate_retrieval_steps(item)
    return ItemSearchResponse(success=True, found=True, item=item, retrievalSteps=retrieval_steps)

@router.post("/retrieve")
async def item_retrieval(request: RetrievalRequest):
    item = get_item_by_id(request.itemId)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item.usageCount += 1
    if item.usageCount >= item.usageLimit:
        item.isWaste = True

    create_log({
        "timestamp": request.timestamp,
        "userId": request.userId,
        "actionType": "retrieval",
        "itemId": request.itemId,
        "details": {"retrieved": True}
    })

    return {"success": True}

def calculate_retrieval_steps(item):
    # Placeholder for an algorithm to calculate retrieval steps
    return [{"step": 1, "action": "retrieve", "itemId": item.id, "itemName": item.name}]
