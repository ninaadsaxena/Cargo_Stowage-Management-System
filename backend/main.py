from fastapi import FastAPI
from api import placement, search, waste, simulation, import_export, logs

app = FastAPI()

app.include_router(placement.router, prefix="/api/placement", tags=["placement"])
app.include_router(search.router, prefix="/api", tags=["search"])
app.include_router(waste.router, prefix="/api/waste", tags=["waste"])
app.include_router(simulation.router, prefix="/api/simulate", tags=["simulation"])
app.include_router(import_export.router, prefix="/api/import", tags=["import_export"])
app.include_router(import_export.router, prefix="/api/export", tags=["import_export"])
app.include_router(logs.router, prefix="/api/logs", tags=["logs"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
