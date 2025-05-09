import redis
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to Redis using the REDIS_URL environment variable
r = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

def set_avg_speed(truck_id, speed_kph):
    r.set(f"truck:{truck_id}:avg_speed", speed_kph)

