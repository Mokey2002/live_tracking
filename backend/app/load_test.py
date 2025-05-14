# locustfile.py
from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(0.5, 1)

    @task
    def get_avg_speed(self):
        self.client.get("/fleet/TRUCK001/avg_speed")

