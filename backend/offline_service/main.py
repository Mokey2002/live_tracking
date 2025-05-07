import time
from checker import check_truck

TRUCK_IDS = [f"TRUCK{i:03}" for i in range(1, 6)]

while True:
    for truck_id in TRUCK_IDS:
        check_truck(truck_id)
    time.sleep(30)

