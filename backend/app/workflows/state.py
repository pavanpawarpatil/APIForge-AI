from typing import TypedDict, Optional, Any


class BackendGenerationState(TypedDict):
    user_request: str

    parsed_request: Optional[Any]

    project_plan: Optional[Any]

    generated_files: Optional[Any]

    validation_result: Optional[Any]

    reviewed_files: Optional[Any]

    output_directory: Optional[str]

    zip_file: Optional[str]
    
    retry_count: int