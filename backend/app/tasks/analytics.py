from app.core.celery_app import celery_app
from app.services.location_cache import get_latest_location
import time

@celery_app.task
def compute_offline_trucks(threshold_seconds=30):
    print("📊 Running offline truck analysis")
    offline_trucks = []

    for truck_id in [f"TRUCK{i:03}" for i in range(1, 6)]:
        loc = get_latest_location(truck_id)
        if loc:
            dt = time.time() - loc["timestamp"]
            if dt > threshold_seconds:
                offline_trucks.append(truck_id)

    print(f"🚨 Offline trucks: {offline_trucks}")
    return offline_trucks

