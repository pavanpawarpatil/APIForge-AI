from app.agents.agent_05_project_builder import (
    project_builder_agent,
)
from app.workflows.state import BackendGenerationState


def builder_node(
    state: BackendGenerationState,
) -> BackendGenerationState:

    project_name = (
        state["parsed_request"].project_name
    )

    project_builder_agent.initialize_project(
        project_name
    )

    generated_files = state["generated_files"]

    for generated_file in generated_files:

        project_builder_agent.run(
            generated_file
        )

    state["output_directory"] = (
        project_builder_agent.get_output_directory()
    )

    return state