from kafka import KafkaConsumer
from redis_client import set_avg_speed
import json, time, math, threading
import uvicorn
from server import app  # this must be after Redis is initialized

locations = {}

def haversine(lat1, lon1, lat2, lon2):
    R = 6371e3
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)
    a = math.sin(d_phi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(d_lambda/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

def consume_kafka():
    consumer = KafkaConsumer(
        "truck-locations",
        bootstrap_servers="kafka:9092",
        group_id="avg-speed-service",
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    print("📡 Kafka consumer started...")

    for msg in consumer:
        data = msg.value
        truck_id = data["truck_id"]
        lat, lng, ts = data["lat"], data["lng"], data["timestamp"]

        if truck_id in locations:
            prev_lat, prev_lng, prev_ts, total_dist, total_time = locations[truck_id]
            dt = ts - prev_ts
            if dt > 0:
                dist = haversine(prev_lat, prev_lng, lat, lng)
                total_dist += dist
                total_time += dt
                avg_speed = (total_dist / total_time) * 3.6
                set_avg_speed(truck_id, round(avg_speed, 2))
                locations[truck_id] = (lat, lng, ts, total_dist, total_time)
        else:
            locations[truck_id] = (lat, lng, ts, 0, 0)

if __name__ == "__main__":
    threading.Thread(target=consume_kafka).start()
    uvicorn.run(app, host="0.0.0.0", port=9001)

