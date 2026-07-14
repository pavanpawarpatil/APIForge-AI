from pydantic import BaseModel, Field


class ValidationResult(BaseModel):
    """
    Represents the validation result
    for generated source code.
    """

    valid: bool

    syntax_errors: list[str] = Field(default_factory=list)

    import_errors: list[str] = Field(default_factory=list)

    style_warnings: list[str] = Field(default_factory=list)

    security_warnings: list[str] = Field(default_factory=list)

    dependency_warnings: list[str] = Field(default_factory=list)