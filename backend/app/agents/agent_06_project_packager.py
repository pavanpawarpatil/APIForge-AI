from pathlib import Path

from app.services.project_packager import (
    project_packager,
)


class ProjectPackagerAgent:
    """
    Packages the generated project.
    """

    def run(
        self,
        project_directory: Path,
    ) -> Path:

        return project_packager.package_project(
            project_directory
        )


project_packager_agent = ProjectPackagerAgent()