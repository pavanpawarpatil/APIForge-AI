from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.models import project
from app.api.project_routes import router as project_router
from app.core.config import settings
from app.database.base import Base
from app.database.connection import engine
from app.api.generator_routes import router as generator_router
from app.api.download_routes import router as download_router
from fastapi.middleware.cors import CORSMiddleware




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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(project_router)
app.include_router(generator_router)
app.include_router(download_router)

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