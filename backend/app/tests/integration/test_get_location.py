from fastapi.testclient import TestClient
from app.main import app
import redis
import json
#works by itself but now when i run all the tests "pytest app/tests/
r = redis.Redis.from_url("redis://localhost:6379")
print("🧪 Imported app from:", app)
for route in app.routes:
    print(f"🛣️  {route.path}")
client = TestClient(app)

def test_redis_ping():
    assert r.ping() == True
def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200

def test_get_location():
    payload = {
        "truck_id": "TRUCK001",
        "lat": 37.78,
        "lng": -122.4,
        "timestamp": 1234567890.0
    }
    r.set("truck:TRUCK001:latest", json.dumps(payload))

    response = client.get("/fleet/TRUCK001/location")
    assert response.status_code == 200
    assert response.json()["lat"] == 37.78

