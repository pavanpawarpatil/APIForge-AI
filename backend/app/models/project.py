from datetime import datetime
from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class Project(Base):
    """
    Represents a generated backend project.
    """
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True
    )
    
    project_name: Mapped[str] = mapped_column(
        String(200), nullable=False
    )
    
    framework: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    database: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    llm: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="Created"
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )