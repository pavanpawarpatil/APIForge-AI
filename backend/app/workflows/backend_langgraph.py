import logging
from langgraph.graph import StateGraph, START, END

from app.workflows.state import BackendGenerationState
from app.workflows.nodes import (
    parser_node, 
    planner_node, 
    generator_node,
    validator_node,
    builder_node,
    reviewer_node,
    packager_node,
    )
from app.workflows.routing import validation_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

graph = StateGraph(BackendGenerationState)

graph.add_node("parser", parser_node)
graph.add_node("planner", planner_node)
graph.add_node("generator", generator_node)
graph.add_node("validator", validator_node)
graph.add_node("builder", builder_node)
graph.add_node("reviewer", reviewer_node)
graph.add_node("packager", packager_node)

graph.add_edge(START, "parser")
graph.add_edge("parser", "planner")
graph.add_edge("planner", "generator")
graph.add_edge("generator", "validator")
graph.add_conditional_edges(
    "validator",
    validation_router,
)
graph.add_edge("builder", "packager")
graph.add_edge("reviewer", "validator")
graph.add_edge("packager", END)

app = graph.compile()

def create_initial_state(user_request: str) -> BackendGenerationState:
    return {
        "user_request": user_request,
        "parsed_request": None,
        "project_plan": None,
        "generated_files": None,
        "validation_result": None,
        "reviewed_files": None,
        "output_directory": None,
        "zip_file": None,
        "retry_count": 0,
    }

if __name__ == "__main__":
    request = """
    Create a FastAPI Todo API.

    CRUD:
    - Create Task
    - Get Task

    Generate the backend.
    """

    result = app.invoke(
        create_initial_state(request)
    )

    print(result)