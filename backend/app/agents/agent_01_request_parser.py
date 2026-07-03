from app.services.llm_service import llm
from app.utils.prompt_loader import load_prompt

class RequestParserAgent:
    """
    Parser the user's request into a structured format.
    """
    def parse(self, user_request: str):
        system_prompt = load_prompt("system_prompt.txt")
        
        parser_prompt = """
        {system_prompt}
        Convert the following user request into structured JSON.
        
        User Request:
        {user_request}
        
        Return only valid JSON 
        """
        response = llm.invoke(parser_prompt)
        return response.content