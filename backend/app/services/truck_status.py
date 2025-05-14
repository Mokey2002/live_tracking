import time

def is_truck_offline(last_seen_timestamp, threshold_seconds=30):
    return (time.time() - last_seen_timestamp) > threshold_seconds

