import time
from app.agents.agent_01_request_parser import (
    request_parser_agent,
)

from app.agents.agent_02_project_planner import (
    project_planner_agent,
)

from app.agents.agent_03_file_generator import (
    file_generator_agent,
)

from app.agents.agent_05_project_builder import (
    project_builder_agent,
)

from app.agents.agent_06_project_packager import (
    project_packager_agent,
)

from app.services.validation_service import (
    validation_service,
)

from app.agents.agent_04_code_reviewer import (
    code_reviewer_agent,
)


class BackendGenerationWorkflow:
    """
    Orchestrates the complete backend
    generation process.
    """

    def _build_section(
        self,
        parsed_request,
        project_plan,
        items,
    ):

        generated_files = []

        total = len(items)

        for index, item in enumerate(items, start=1):

            print(f"   [{index}/{total}] {item.path}")

            generated = file_generator_agent.run(
                parsed_request,
                project_plan,
                item,
            )


            validation = validation_service.validate(
                generated.source_code
            )

            if validation.valid:


                project_builder_agent.run(
                    generated
                )

            else:
                reviewed = code_reviewer_agent.run(
                    generated,
                    validation,
                )

                generated.source_code = (
                    reviewed.reviewed_source_code
                )

                project_builder_agent.run(
                    generated
                )

            generated_files.append(
                generated
            )

        return generated_files

    def run(
        self,
        user_request: str,
    ):

        start_time = time.time()

        print("\n" + "=" * 60)
        print("APIForge AI")
        print("=" * 60)

        print("\n[1] Parsing request...")
        parsed_request = request_parser_agent.run(
            user_request
        )
        print("✓ Request parsed")

        print("\n[2] Planning project...")
        project_plan = project_planner_agent.run(
            parsed_request
        )
        print("✓ Project planned")

        print("\n[3] Initializing project...")

        project_directory = (
            project_builder_agent.initialize_project(
                parsed_request.project_name
            )
        )

        print(f"✓ Project directory: {project_directory}")

        generated_files = []

        sections = [
            ("Files", project_plan.files),
            ("Models", project_plan.models),
            ("API Routes", project_plan.api_routes),
            ("Services", project_plan.services),
            ("Schemas", project_plan.schemas),
        ]

        for section_name, items in sections:

            print(f"\nGenerating {section_name}...")

            generated_files.extend(
                self._build_section(
                    parsed_request,
                    project_plan,
                    items,
                )
            )

            print(f"✓ {section_name} completed")

        print("\nPackaging project...")

        zip_file = project_packager_agent.run(
            project_builder_agent.get_output_directory()
        )

        print("✓ Project packaged")

        total_time = time.time() - start_time

        print("\n" + "=" * 60)
        print("PROJECT GENERATED SUCCESSFULLY")
        print("=" * 60)
        print(f"Generated Files : {len(generated_files)}")
        print(f"Time Taken      : {total_time:.2f} seconds")

        return generated_files


backend_generation_workflow = BackendGenerationWorkflow()