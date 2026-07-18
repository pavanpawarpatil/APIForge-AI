import logging

from app.agents.agent_01_request_parser import RequestParserAgent
from app.workflows.state import BackendGenerationState

logger = logging.getLogger(__name__)

request_parser_agent = RequestParserAgent()


def parser_node(state: BackendGenerationState) -> BackendGenerationState:

    logger.info("Starting Request Parser Agent...")

    state["parsed_request"] = request_parser_agent.run(
        state["user_request"]
    )

    logger.info("Request Parser Agent completed successfully.")

    return state