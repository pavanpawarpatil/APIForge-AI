from app.services.validation_service import validation_service
from app.workflows.state import BackendGenerationState


def validator_node(
    state: BackendGenerationState,
) -> BackendGenerationState:

    generated_files = state["generated_files"]

    validation_results = []

    for generated_file in generated_files:

        result = validation_service.validate(
            generated_file.source_code
        )

        validation_results.append(result)

    state["validation_result"] = validation_results

    return state