from pydantic import BaseModel


class ProjectItem(BaseModel):
    """
    Represents one project component.
    """

    name: str

    path: str

    purpose: str


class ProjectPlanResponse(BaseModel):
    """
    Structured output from Agent 02.
    """

    folders: list[str]

    files: list[ProjectItem]

    models: list[ProjectItem]

    api_routes: list[ProjectItem]

    services: list[ProjectItem]

    schemas: list[ProjectItem]

    python_dependencies: list[str]

    infrastructure: list[str]