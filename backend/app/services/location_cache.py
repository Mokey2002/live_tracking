import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to Redis
r = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

def set_latest_location(truck_id: str, data: dict):
    r.set(f"truck:{truck_id}:latest", json.dumps(data))

def get_latest_location(truck_id: str):
    raw = r.get(f"truck:{truck_id}:latest")
    return json.loads(raw) if raw else None

