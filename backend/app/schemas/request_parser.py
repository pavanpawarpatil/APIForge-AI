from typing import Optional

from pydantic import BaseModel


class RequestParserResponse(BaseModel):
    """
    Structured output from Agent 01.
    """

    project_name: Optional[str] = None
    framework: Optional[str] = None
    database: Optional[str] = None
    authentication: Optional[str] = None

    docker: Optional[bool] = False
    redis: Optional[bool] = False

    features: list[str] = []