from pydantic import BaseModel


class ReviewedCode(BaseModel):
    """
    Represents reviewed and improved
    source code.
    """

    filename: str

    filepath: str

    reviewed_source_code: str