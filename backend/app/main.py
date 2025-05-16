# backend/app/main.py
from fastapi import FastAPI
from app.api.routes import fleet
from app.tasks.analytics import compute_offline_trucks  # 👈 import task

app = FastAPI(title="FleetOps API")

# Include API routers
app.include_router(fleet.router, prefix="/fleet", tags=["Fleet"])

# ✅ Analytics route registered directly
@app.get("/analytics/offline")
def trigger_offline_analysis():
    compute_offline_trucks.delay()
    return {"msg": "Offline truck analysis started"}

@app.get("/")
def root():
    return {"message": "FleetOps API is running"}

@app.get("/ping")
def ping():
    return {"msg": "pong"}

