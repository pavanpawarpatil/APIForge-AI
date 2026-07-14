import json
import re
from typing import Any


def parse_llm_json(response: str) -> dict[str, Any]:
    """
    Parse JSON returned by an LLM.

    This function automatically removes Markdown code fences
    and extracts the JSON object before parsing.
    """

    if not response:
        raise ValueError("LLM returned an empty response.")

    # Remove ```json and ```
    cleaned = re.sub(
        r"^```(?:json)?|```$",
        "",
        response.strip(),
        flags=re.MULTILINE,
    ).strip()

    # Extract first JSON object
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)

    if not match:
        raise ValueError("No valid JSON object found in LLM response.")

    json_string = match.group()

    try:
        return json.loads(json_string)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON returned by LLM.\n{error}"
        ) from error