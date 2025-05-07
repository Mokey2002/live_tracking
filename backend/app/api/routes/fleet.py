# backend/app/api/routes/fleet.py
from fastapi import APIRouter
from app.services.location_cache import get_latest_location, get_truck_status

router = APIRouter()

@router.get("/")
def list_trucks():
    return [{"truck_id": "TRUCK123", "status": "active"}]

@router.get("/{truck_id}/location")
def get_truck_location(truck_id: str):
    location = get_latest_location(truck_id)
    if not location:
        return {"error": "No data for this truck"}
    return location
    
@router.get("/{truck_id}/status")
def get_truck_status_route(truck_id: str):
    status = get_truck_status(truck_id)
    return {"truck_id": truck_id, "status": status or "unknown"}

