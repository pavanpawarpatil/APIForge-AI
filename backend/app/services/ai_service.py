from typing import Type

from pydantic import BaseModel

from app.services.llm_service import llm
from app.utils.json_parser import parse_llm_json

class AIService:
    """
    High-level AI service responsible for
    interacting with the LLM and returning
    validated responses.
    """

    def generate_text(self, prompt: str) -> str:
        """
        Generate plain text from the LLM.
        """
        response = llm.invoke(prompt)
        return response.content

    def generate_json(self, prompt: str) -> dict:
        """
        Generate JSON from the LLM.
        """
        response = llm.invoke(prompt)
        return parse_llm_json(response.content)

    def generate_structured(
        self,
        prompt: str,
        schema: Type[BaseModel],
    ) -> BaseModel:
        """
        Generate a validated Pydantic model.
        """

        data = self.generate_json(prompt)

        return schema(**data)


ai_service = AIService()