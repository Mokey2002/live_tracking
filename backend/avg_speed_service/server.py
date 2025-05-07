from fastapi import FastAPI
from redis_client import r

app = FastAPI()

@app.get("/avg_speed/{truck_id}")
def get_avg_speed(truck_id: str):
    speed = r.get(f"truck:{truck_id}:avg_speed")
    return {
        "truck_id": truck_id,
        "avg_speed_kph": float(speed) if speed else None
    }

