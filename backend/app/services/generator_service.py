from pathlib import Path
from app.schemas.generator import GenerateRequest, GenerateResponse
from app.workflows.backend_langgraph import app, create_initial_state


class GeneratorService:

    @staticmethod
    def generate_backend(request: GenerateRequest) -> GenerateResponse:

        result = app.invoke(
            create_initial_state(request.prompt)
        )

        parsed_request = result["parsed_request"]
        zip_name = Path(result["zip_file"]).name

        return GenerateResponse(
            success=True,
            message="Backend generated successfully.",
            project_name=parsed_request.project_name,
            zip_file=zip_name,
        )