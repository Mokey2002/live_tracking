from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

celery_app = Celery(
    "fleetops",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery_app.conf.task_routes = {
    "app.tasks.analytics.*": {"queue": "analytics"}
}

