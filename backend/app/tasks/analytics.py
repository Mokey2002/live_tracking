# app/tasks/analytics.py
from celery import shared_task
import redis
import json

r = redis.Redis.from_url("redis://redis:6379")

@shared_task
def compute_offline_trucks(threshold_seconds=30):
    offline = []
    for key in r.scan_iter("truck:*:latest"):
        data = json.loads(r.get(key))
        if time.time() - data["timestamp"] > threshold_seconds:
            offline.append(data["truck_id"])
    return offline

