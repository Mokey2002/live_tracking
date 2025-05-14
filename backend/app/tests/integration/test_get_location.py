# tests/integration/test_get_location.py
from fastapi.testclient import TestClient
from main import app
import redis
import json

r = redis.Redis.from_url("redis://localhost:6379")
print("🔍 Connected to Redis:", r.ping())
client = TestClient(app)
def test_redis_ping():
    r = redis.Redis.from_url("redis://localhost:6379")
    assert r.ping() == True
    
def test_get_location():
    payload = {"truck_id": "TRUCK001", "lat": 37.78, "lng": -122.4, "timestamp": 1234567890.0}
    r.set("truck:TRUCK001:latest", json.dumps(payload))

    response = client.get("/fleet/TRUCK001/location")
    assert response.status_code == 200
    assert response.json()["lat"] == 37.78

