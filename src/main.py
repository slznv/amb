import sys

from fastapi import FastAPI
from loguru import logger
import uvicorn

import config
from api.v1.routes import api_router
from config import LOG_LEVEL, LOG_AS_JSON
from storage.main import storage


def setup_logging():
    logger.remove()
    is_debug = LOG_LEVEL == "DEBUG"
    logger.add(
        sys.stdout, colorize=False, level=LOG_LEVEL,
        serialize=LOG_AS_JSON,
        backtrace=is_debug, diagnose=is_debug
    )


def setup_storage():
    """Here we can decide which type of storage to use base on config"""
    if config.STORAGE == "IN_MEMORY":
        from storage.in_memory import InMemoryStorage
        storage.storage = InMemoryStorage()
        return

    raise RuntimeError("No storage configured")


app = FastAPI(
    title="Graphs",
    docs_url=None,
    redoc_url=None,
)

app.include_router(api_router, prefix="/v1")


if __name__ == "__main__":
    setup_logging()
    setup_storage()
    uvicorn.run(app, host="0.0.0.0", port=8000)
