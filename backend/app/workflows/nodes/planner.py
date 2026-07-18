from app.agents.agent_02_project_planner import ProjectPlannerAgent
from app.workflows.state import BackendGenerationState

project_planner_agent = ProjectPlannerAgent()


def planner_node(
    state: BackendGenerationState,
) -> BackendGenerationState:

    parsed_request = state["parsed_request"]

    project_plan = project_planner_agent.run(parsed_request)

    state["project_plan"] = project_plan

    return state