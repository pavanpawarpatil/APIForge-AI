from app.agents.agent_03_file_generator import FileGeneratorAgent
from app.workflows.state import BackendGenerationState

file_generator_agent = FileGeneratorAgent()


def generator_node(
    state: BackendGenerationState,
) -> BackendGenerationState:

    request = state["parsed_request"]
    project = state["project_plan"]

    all_files = (
        project.files
        + project.models
        + project.api_routes
        + project.services
        + project.schemas
    )

    generated_files = []

    for file in all_files:
        generated_code = file_generator_agent.run(
            request=request,
            project=project,
            file=file,
        )

        generated_files.append(generated_code)

    state["generated_files"] = generated_files

    return state