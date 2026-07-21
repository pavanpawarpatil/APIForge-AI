from pydantic import BaseModel


class GenerateRequest(BaseModel):
    prompt: str


class GenerateResponse(BaseModel):
    success: bool
    message: str
    project_name: str | None = None
    zip_file: str | None = None