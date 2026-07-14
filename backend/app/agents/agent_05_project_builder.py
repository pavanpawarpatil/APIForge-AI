from pathlib import Path

from app.schemas.file_generator import GeneratedCode
from app.services.project_builder import project_builder


class ProjectBuilderAgent:
    """
    Agent responsible for building
    the generated project.
    """

    def initialize_project(
        self,
        project_name: str,
    ) -> Path:
        """
        Initialize the project directory.
        """

        return project_builder.set_project_directory(
            project_name
        )

    def run(
        self,
        generated_file: GeneratedCode,
    ) -> Path:

        return project_builder.build_file(
            generated_file
        )

    def get_output_directory(
        self,
    ) -> Path:
        """
        Return the generated project directory.
        """

        return project_builder.get_output_directory()


project_builder_agent = ProjectBuilderAgent()