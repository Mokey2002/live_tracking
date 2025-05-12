from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9094",  # use 'kafka:9092' if running inside Docker
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TRUCK_IDS = [f"TRUCK{i:03}" for i in range(1, 4)]

def generate_data(truck_id):
    return {
        "truck_id": truck_id,
        "lat": round(random.uniform(37.75, 37.80), 5),
        "lng": round(random.uniform(-122.45, -122.40), 5),
        "timestamp": time.time()
    }

while True:
    for truck_id in TRUCK_IDS:
        payload = generate_data(truck_id)
        producer.send("truck-locations", value=payload)
        print("📤 Sent:", payload)
    time.sleep(0.5)  # Send all trucks every 0.5s (~10 messages/sec total)

