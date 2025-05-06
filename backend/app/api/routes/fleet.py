# backend/app/api/routes/fleet.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_trucks():
    return [{"truck_id": "TRUCK123", "status": "active"}]

