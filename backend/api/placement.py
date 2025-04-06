from fastapi import APIRouter, HTTPException
from typing import List
from schemas import PlacementRequest
from models import Item, Container
from crud import create_item, create_container, get_container_by_id

router = APIRouter()

@router.post("/")
async def placement_recommendation(request: PlacementRequest):
    placements = []
    rearrangements = []

    for item in request.items:
        create_item(item)
        container = find_optimal_container(item, request.containers)
        if container:
            position = find_optimal_position(item, container)
            placements.append({
                "itemId": item.itemId,
                "containerId": container.containerId,
                "position": {
                    "startCoordinates": {"width": position[0], "depth": position[1], "height": position[2]},
                    "endCoordinates": {"width": position[0] + item.width, "depth": position[1] + item.depth, "height": position[2] + item.height}
                }
            })
            update_container_utilization(container.containerId)
        else:
            rearrangements.append({
                "action": "rearrange",
                "itemId": item.itemId,
                "reason": "No optimal container found"
            })

    return {"success": True, "placements": placements, "rearrangements": rearrangements}

def find_optimal_container(item: Item, containers: List[Container]) -> Optional[Container]:
    available_containers = [c for c in containers if c.zone == item.preferredZone or c.spaceUtilization < 80]
    available_containers.sort(key=lambda c: c.spaceUtilization)
    for container in available_containers:
        if item.width <= container.width and item.depth <= container.depth and item.height <= container.height:
            return container
    return None

def find_optimal_position(item: Item, container: Container) -> dict:
    return {"x": 0, "y": 0, "z": 0}  # Simplified for demonstration

def update_container_utilization(container_id: str):
    container = get_container_by_id(container_id)
    if container:
        container.spaceUtilization += 10  # Simplified for demonstration
        update_container(container_id, container)
