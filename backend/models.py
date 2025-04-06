from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Item(BaseModel):
    itemId: str
    name: str
    width: float
    depth: float
    height: float
    priority: int
    expiryDate: Optional[str]
    usageLimit: int
    preferredZone: str

class Container(BaseModel):
    containerId: str
    zone: str
    width: float
    depth: float
    height: float

class Log(BaseModel):
    timestamp: str
    userId: str
    actionType: str
    itemId: str
    details: dict
