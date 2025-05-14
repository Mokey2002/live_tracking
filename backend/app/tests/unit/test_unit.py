import time
from services.truck_status import is_truck_offline

def test_truck_is_offline():
    past = time.time() - 40  # 40 seconds ago
    assert is_truck_offline(past) == True

def test_truck_is_online():
    recent = time.time() - 10  # 10 seconds ago
    assert is_truck_offline(recent) == False

