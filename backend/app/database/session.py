from collections.abc import Generator

from sqlalchemy.orm import Session, sessionmaker

from app.database.connection import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db() -> Generator[Session, None, None]:
    """
    Creates a new database session for each request
    and closes it automatically after the request finishes.
    """
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()