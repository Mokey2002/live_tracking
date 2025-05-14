import requests
import time

BASE_URL = "http://localhost:8000"

def test_avg_speed_flow():
    truck_id = "TRUCK002"
    
    # Give time for the system to process Kafka messages
    time.sleep(5)

    response = requests.get(f"{BASE_URL}/fleet/{truck_id}/avg_speed")
    assert response.status_code == 200
    data = response.json()
    assert data["truck_id"] == truck_id
    assert isinstance(data["avg_speed_kph"], (float, int))

