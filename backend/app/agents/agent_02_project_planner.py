from app.schemas.project_planner import ProjectPlanResponse
from app.schemas.request_parser import RequestParserResponse
from app.services.ai_service import ai_service
from app.utils.prompt_loader import load_prompt


class ProjectPlannerAgent:
    """
    Creates the implementation plan
    for the backend project.
    """

    def __init__(self):
        self.prompt_template = load_prompt(
            "02_project_planner.txt"
        )

    def run(
        self,
        parsed_request: RequestParserResponse,
    ) -> ProjectPlanResponse:

        prompt = (
            f"{self.prompt_template}\n\n"
            f"{parsed_request.model_dump_json(indent=4)}"
        )

        return ai_service.generate_structured(
            prompt=prompt,
            schema=ProjectPlanResponse,
        )


project_planner_agent = ProjectPlannerAgent()