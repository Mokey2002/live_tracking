from kafka import KafkaConsumer
import json
import os

# Optional: load environment variables
from dotenv import load_dotenv
load_dotenv(dotenv_path="/home/ed/Desktop/gps_vehicle_tracking/backend/.env")
print("🔍 KAFKA_BOOTSTRAP_SERVERS =", os.getenv("KAFKA_BOOTSTRAP_SERVERS"))
if os.path.exists("/.dockerenv"):
    print("🪵 Running INSIDE Docker container")
else:
    print("💻 Running OUTSIDE Docker container")
from app.services.location_cache import set_latest_location

load_dotenv()

BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
TOPIC = "truck-locations"
def safe_deserializer(m):
    try:
        return json.loads(m.decode('utf-8'))
    except Exception as e:
        print(f"❌ Failed to decode message: {m} — {e}")
        return None

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',
    group_id='location-tracker',
    value_deserializer=safe_deserializer
)


print("✅ Kafka consumer started...")

for msg in consumer:
    location = msg.value
    print(f"📦 Received: {location}")
    #saves to redis
    set_latest_location(location["truck_id"], location)
