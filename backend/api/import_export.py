from fastapi import APIRouter, UploadFile, File
from schemas import ImportResponse
from crud import create_item, create_container, query_db
import csv

router = APIRouter()

@router.post("/items")
async def import_items(file: UploadFile = File(...)):
    results = []
    errors = []
    row_count = 0

    with open(file.file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_count += 1
            try:
                item = {
                    "id": row["ItemID"],
                    "name": row["Name"],
                    "width": float(row["Width"]),
                    "depth": float(row["Depth"]),
                    "height": float(row["Height"]),
                    "priority": int(row["Priority"]),
                    "expiryDate": row["ExpiryDate"] if row["ExpiryDate"] != 'N/A' else None,
                    "usageLimit": int(row["UsageLimit"]) if row["UsageLimit"] != 'N/A' else None,
                    "usageCount": int(row["UsageCount"]) if row["UsageCount"] else 0,
                    "preferredZone": row["PreferredZone"],
                    "isWaste": False
                }
                create_item(item)
                results.append(item)
            except Exception as e:
                errors.append({"row": row_count, "message": str(e)})

    return ImportResponse(success=True, itemsImported=len(results), errors=errors)

@router.post("/containers")
async def import_containers(file: UploadFile = File(...)):
    results = []
    errors = []
    row_count = 0

    with open(file.file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_count += 1
            try:
                container = {
                    "id": row["ContainerID"],
                    "zone": row["Zone"],
                    "width": float(row["Width"]),
                    "depth": float(row["Depth"]),
                    "height": float(row["Height"]),
                    "spaceUtilization": 0
                }
                create_container(container)
                results.append(container)
            except Exception as e:
                errors.append({"row": row_count, "message": str(e)})

    return ImportResponse(success=True, containersImported=len(results), errors=errors)

@router.get("/arrangement")
async def export_arrangement():
    items = query_db('SELECT * FROM items')
    csv_content = "Item ID,Container ID,Coordinates (W1,D1,H1),(W2,D2,H2)\n"
    for item in items:
        if item["containerId"]:
            csv_content += f'{item["id"]},{item["containerId"]},({item["x"]},{item["y"]},{item["z"]}),({item["x"] + item["width"]},{item["y"] + item["depth"]},{item["z"] + item["height"]})\n'
    return csv_content
