# backend/app/main.py
from fastapi import FastAPI
from app.api.routes import fleet

app = FastAPI(title="FleetOps API")

# Include route groups
app.include_router(fleet.router, prefix="/fleet", tags=["Fleet"])
#app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])

@app.get("/")
def root():
    return {"message": "FleetOps API is running"}

