from app.workflows.state import BackendGenerationState

MAX_RETRIES = 3


def validation_router(
    state: BackendGenerationState,
) -> str:

    validation_results = state["validation_result"]

    all_valid = all(
        result.valid
        for result in validation_results
    )

    if all_valid:
        return "builder"

    retry_count = state.get("retry_count", 0)

    if retry_count >= MAX_RETRIES:
        print("Maximum retry limit reached.")
        return "builder"

    return "reviewer"