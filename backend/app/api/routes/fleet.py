# backend/app/api/routes/fleet.py
from fastapi import APIRouter
from app.services.location_cache import get_latest_location, get_truck_status
import requests
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

@router.get("/{truck_id}/avg_speed")
def get_avg_speed_via_microservice(truck_id: str):
    try:
        res = requests.get(f"http://avg-speed-service:9001/avg_speed/{truck_id}", timeout=2)
        res.raise_for_status()  # raise an error for 5xx or 4xx responses
        return res.json()
    except requests.exceptions.RequestException as e:
        return {
            "truck_id": truck_id,
            "avg_speed_kph": None,
            "error": str(e)
        }
