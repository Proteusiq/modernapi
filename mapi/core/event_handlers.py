from typing import Callable

from fastapi import FastAPI

from mapi.database.session import engine
from mapi.database.configuration import setup_db


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        # logging.info("Running app start handler.")
        setup_db(engine)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        # logging.info("Running app shutdown handler.")
        pass

    return shutdown
