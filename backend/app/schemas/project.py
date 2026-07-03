from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProjectCreate(BaseModel):
    project_name: str
    framework: str
    database: str
    llm: str


class ProjectResponse(BaseModel):
    id: int
    project_name: str
    framework: str
    database: str
    llm: str
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)