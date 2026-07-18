from app.agents.agent_06_project_packager import (
    project_packager_agent,
)

from app.workflows.state import (
    BackendGenerationState,
)

def packager_node(
    state: BackendGenerationState,
):

    output_directory = state["output_directory"]

    zip_file = project_packager_agent.run(
        output_directory
    )

    state["zip_file"] = zip_file

    return state