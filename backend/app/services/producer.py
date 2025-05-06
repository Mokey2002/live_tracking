from kafka import KafkaProducer
import json
import time
import random

# Simulated list of truck IDs
TRUCK_IDS = [f"TRUCK{i:03}" for i in range(1, 6)]  # TRUCK001 to TRUCK005

# Kafka setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Frequency (seconds between messages per truck)
MESSAGE_INTERVAL = 1.0

print("🚛 Starting producer for multiple trucks...")

while True:
    for truck_id in TRUCK_IDS:
        message = {
            "truck_id": truck_id,
            "lat": round(random.uniform(37.7, 37.9), 5),
            "lng": round(random.uniform(-122.5, -122.3), 5),
            "timestamp": time.time()
        }
        print(f"📤 Sending: {message}")
        producer.send("truck-locations", value=message)
    producer.flush()
    time.sleep(MESSAGE_INTERVAL)

