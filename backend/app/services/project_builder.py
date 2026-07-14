from pathlib import Path

from app.schemas.file_generator import GeneratedCode


class ProjectBuilder:
    """
    Creates folders and writes generated files
    to the output project.
    """

    def __init__(
        self,
        output_root: str = "generated_projects",
    ):
        self.output_root = Path(output_root)
        self.project_directory: Path | None = None

    def set_project_directory(
        self,
        project_name: str,
    ) -> Path:
        """
        Create a project-specific output directory.
        """

        safe_name = (
            project_name.lower()
            .replace(" ", "_")
            .replace("-", "_")
        )

        self.project_directory = (
            self.output_root / safe_name
        )

        self.project_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        return self.project_directory

    def build_file(
        self,
        generated_file: GeneratedCode,
    ) -> Path:
        """
        Create directories and write one file.
        """

        if self.project_directory is None:
            raise RuntimeError(
                "Project directory has not been initialized."
            )

        file_path = (
            self.project_directory
            / generated_file.filepath
        )

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path.write_text(
            generated_file.source_code,
            encoding="utf-8",
        )

        return file_path

    def get_output_directory(
        self,
    ) -> Path:
        """
        Return the generated project directory.
        """

        if self.project_directory is None:
            raise RuntimeError(
                "Project directory has not been initialized."
            )

        return self.project_directory


project_builder = ProjectBuilder()