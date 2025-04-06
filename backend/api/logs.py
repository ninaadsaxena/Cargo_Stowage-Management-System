from fastapi import APIRouter
from typing import Optional
from crud import get_logs

router = APIRouter()

@router.get("/")
async def get_logs(startDate: Optional[str] = None, endDate: Optional[str] = None, itemId: Optional[str] = None, userId: Optional[str] = None, actionType: Optional[str] = None):
    logs = get_logs()
    if startDate:
        logs = [log for log in logs if log.timestamp >= startDate]
    if endDate:
        logs = [log for log in logs if log.timestamp <= endDate]
    if itemId:
        logs = [log for log in logs if log.itemId == itemId]
    if userId:
        logs = [log for log in logs if log.userId == userId]
    if actionType:
        logs = [log for log in logs if log.actionType == actionType]
    return {"logs": logs}
