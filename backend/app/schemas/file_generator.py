from pydantic import BaseModel


class GeneratedCode(BaseModel):
    """
    Represents the generated source code
    for a single project file.
    """

    filename: str

    filepath: str

    source_code: str