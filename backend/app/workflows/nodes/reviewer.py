from app.agents.agent_04_code_reviewer import (
    code_reviewer_agent,
)
from app.workflows.state import BackendGenerationState


def reviewer_node(
    state: BackendGenerationState,
) -> BackendGenerationState:

    generated_files = state["generated_files"]

    validation_results = state["validation_result"]

    reviewed_files = []

    for generated_file, validation in zip(
        generated_files,
        validation_results,
    ):

        if validation.valid:

            reviewed_files.append(
                generated_file
            )

        else:

            reviewed_code = code_reviewer_agent.run(
                generated_code=generated_file,
                validation=validation,
            )

            reviewed_files.append(
                reviewed_code
            )

    state["reviewed_files"] = reviewed_files

    state["generated_files"] = reviewed_files
    
    state["retry_count"] += 1

    return state