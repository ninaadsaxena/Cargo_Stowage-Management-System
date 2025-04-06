from pydantic import BaseModel
from typing import List, Optional
from models import Item, Container

class PlacementRequest(BaseModel):
    items: List[Item]
    containers: List[Container]

class ItemSearchResponse(BaseModel):
    success: bool
    found: bool
    item: Optional[Item]
    retrievalSteps: Optional[List[dict]]

class RetrievalRequest(BaseModel):
    itemId: str
    userId: str
    timestamp: str

class PlacementRequest(BaseModel):
    itemId: str
    userId: str
    timestamp: str
    containerId: str
    position: dict

class WasteIdentificationResponse(BaseModel):
    success: bool
    wasteItems: List[Item]

class WasteReturnPlanRequest(BaseModel):
    undockingContainerId: str
    undockingDate: str
    maxWeight: float

class WasteReturnPlanResponse(BaseModel):
    success: bool
    returnPlan: List[dict]
    retrievalSteps: List[dict]
    returnManifest: dict

class SimulationRequest(BaseModel):
    numOfDays: Optional[int]
    toTimestamp: Optional[str]
    itemsToBeUsedPerDay: List[dict]

class SimulationResponse(BaseModel):
    success: bool
    newDate: str
    changes: dict

class ImportResponse(BaseModel):
    success: bool
    itemsImported: int
    errors: List[dict]
