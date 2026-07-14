from app.schemas.file_generator import GeneratedCode
from app.schemas.project_planner import (
    ProjectItem,
    ProjectPlanResponse,
)
from app.services.code_cleaner import code_cleaner
from app.schemas.request_parser import RequestParserResponse
from app.services.ai_service import ai_service
from app.utils.prompt_loader import load_prompt


class FileGeneratorAgent:
    """
    Generates the source code
    for a single project file.
    """

    def __init__(self):
        self.prompt_template = load_prompt(
            "03_file_generator.txt"
        )

    def run(
        self,
        request: RequestParserResponse,
        project: ProjectPlanResponse,
        file: ProjectItem,
    ) -> GeneratedCode:

        prompt = f"""
{self.prompt_template}

PROJECT REQUIREMENTS

{request.model_dump_json(indent=4)}

PROJECT BLUEPRINT

{project.model_dump_json(indent=4)}

TARGET FILE

Name:
{file.name}

Path:
{file.path}

Purpose:
{file.purpose}
"""

        source_code = ai_service.generate_text(prompt)

        source_code = code_cleaner.clean(
            source_code
        )
        
        generated_code = """
        from fastapi import FastAPI

        app = FastAPI(

        @app.get("/")
        def home():
            return {"message": "Hello"}
        """
        
        return GeneratedCode(
            filename=file.name,
            filepath=file.path,
            source_code=source_code,
        )


file_generator_agent = FileGeneratorAgent()