from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.database.connection import engine


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

@app.get("/")
def root():
    return{
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
                "Status": "Healthy",
                "database": "Connected"
            }
    except Exception as e:
        return {
            "States": "Unhealthy",
            "database": "Disconnected", 
            "error": str(e)
        }