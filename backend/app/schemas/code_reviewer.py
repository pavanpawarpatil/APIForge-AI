from pydantic import BaseModel


class ReviewedCode(BaseModel):
    """
    Represents reviewed and improved
    source code.
    """

    filename: str

    filepath: str

    source_code: str