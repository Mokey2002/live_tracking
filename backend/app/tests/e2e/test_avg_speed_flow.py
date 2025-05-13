# tests/e2e/test_avg_speed_flow.py
import requests
import time

def test_avg_speed_calculation():
    # Wait for services to stabilize
    time.sleep(10)

    # Send sample location (assumes producer or kafka push already happening)
    response = requests.get("http://localhost:8000/fleet/TRUCK001/avg_speed")
    data = response.json()

    assert response.status_code == 200
    assert data["avg_speed_kph"] is not None
    assert data["avg_speed_kph"] > 0

