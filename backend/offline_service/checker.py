import time
from redis_client import get_latest_location, set_truck_status
from datetime import datetime

def check_truck(truck_id, threshold_seconds=300):
    data = get_latest_location(truck_id)
    if not data:
        return

    now = time.time()
    if now - data["timestamp"] > threshold_seconds:
        print(f"⚠️ {truck_id} is offline!")
        set_truck_status(truck_id, "offline")
    else:
        set_truck_status(truck_id, "online")

