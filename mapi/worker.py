from time import sleep
from os import environ
from celery import Celery

celery = Celery(__name__)

celery.conf.broker_url = environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = environ.get(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379"
)


@celery.task(name="do_this")
def do_this(snooze):
    sleep(snooze)
    return {"message": "the do task is done", "success": True, "snoozed": snooze}


# code to send to minio
