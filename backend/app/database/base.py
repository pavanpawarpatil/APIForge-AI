from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models.

    Every database model in APIForge AI will inherit from this class.
    """
    pass