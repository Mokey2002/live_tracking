from kafka import KafkaConsumer
import json
import os

# Optional: load environment variables
from dotenv import load_dotenv
from app.services.location_cache import set_latest_location

load_dotenv()

BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
TOPIC = "truck-locations"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',
    group_id='location-tracker',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("✅ Kafka consumer started...")

for msg in consumer:
    location = msg.value
    print(f"📦 Received: {location}")
    #saves to redis
    set_latest_location(location["truck_id"], location)
