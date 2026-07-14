from pydantic import BaseModel

from app.schemas.request_parser import RequestParserResponse
from app.schemas.project_planner import ProjectPlanResponse
from app.schemas.file_generator import GeneratedCode
from app.schemas.code_reviewer import ReviewedCode
from app.schemas.validation import ValidationResult


class ProjectContext(BaseModel):

    request: RequestParserResponse

    project_plan: ProjectPlanResponse

    generated_files: list[GeneratedCode] = []

    reviewed_files: list[ReviewedCode] = []

    validations: list[ValidationResult] = []