import redis
import os
import json
from dotenv import load_dotenv

load_dotenv()
r = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

def get_latest_location(truck_id):
    raw = r.get(f"truck:{truck_id}:latest")
    return json.loads(raw) if raw else None

def set_truck_status(truck_id, status):
    r.set(f"truck:{truck_id}:status", status)

