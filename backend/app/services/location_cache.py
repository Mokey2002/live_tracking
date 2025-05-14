import redis
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env") 
#load_dotenv()

# Connect to Redis
r = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

def set_latest_location(truck_id: str, data: dict):
    r.set(f"truck:{truck_id}:latest", json.dumps(data))

def get_latest_location(truck_id: str):

    raw = r.get(f"truck:{truck_id}:latest")
    print(f"🧠 Redis get key: truck:{truck_id}:latest")
    print(f"🧠 Raw value: {raw}")
    return json.loads(raw) if raw else None
    
def get_truck_status(truck_id: str):
    status = r.get(f"truck:{truck_id}:status")
    return status.decode() if status else None

