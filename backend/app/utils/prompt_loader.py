from pathlib import Path

PROMPT_DIR = Path(__file__).parent.parent / "prompts"


def load_prompt(filename: str) -> str:
    """
    Load a prompt template from the prompts directory.
    """
    file_path = PROMPT_DIR / filename
    
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()