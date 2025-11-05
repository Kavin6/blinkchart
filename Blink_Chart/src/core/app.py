from fastapi import FastAPI
from src.routers import health


def create_app() -> FastAPI:
    app = FastAPI(title="my app", version="1.0.0")
    app.include_router(health.router)
    return app
