from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.database.base import Base
from app.database.connection import engine

# Import all models here
from app.models.project import Project


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs once when the application starts.
    """

    # Create database tables
    Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)


@app.get("/")
def root():
    return {
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "model": settings.OLLAMA_MODEL
    }


@app.get("/health")
def health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "Healthy",
            "database": "Connected"
        }

    except Exception as e:
        return {
            "status": "Unhealthy",
            "database": "Disconnected",
            "error": str(e)
        }