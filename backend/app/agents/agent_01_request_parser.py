from app.schemas.request_parser import RequestParserResponse
from app.services.ai_service import ai_service
from app.utils.prompt_loader import load_prompt


class RequestParserAgent:
    """
    Agent responsible for converting
    a natural language request into
    a structured project definition.
    """

    def __init__(self):
        self.prompt_template = load_prompt(
            "01_request_parser.txt"
        )

    def run(
        self,
        user_request: str,
    ) -> RequestParserResponse:

        prompt = (
            f"{self.prompt_template}\n\n"
            f"User Request:\n"
            f"{user_request}"
        )

        return ai_service.generate_structured(
            prompt=prompt,
            schema=RequestParserResponse,
        )


request_parser_agent = RequestParserAgent()