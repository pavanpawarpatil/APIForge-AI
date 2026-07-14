from app.schemas.code_reviewer import ReviewedCode
from app.schemas.file_generator import GeneratedCode
from app.schemas.validation import ValidationResult
from app.services.ai_service import ai_service
from app.utils.prompt_loader import load_prompt
from app.services.code_cleaner import code_cleaner


class CodeReviewerAgent:
    """
    Reviews generated source code and fixes
    validation issues.
    """

    def __init__(self):
        self.prompt_template = load_prompt(
            "04_code_reviewer.txt"
        )

    def run(
        self,
        generated_code: GeneratedCode,
        validation: ValidationResult,
    ) -> ReviewedCode:

        prompt = f"""
{self.prompt_template}

========================================
FILE INFORMATION
========================================

Filename:
{generated_code.filename}

Path:
{generated_code.filepath}

========================================
VALIDATION RESULT
========================================

{validation.model_dump_json(indent=4)}

========================================
SOURCE CODE
========================================

{generated_code.source_code}
"""

        corrected_source = ai_service.generate_text(
            prompt
        )

        corrected_source = code_cleaner.clean(
            corrected_source
        )

        return ReviewedCode(
            filename=generated_code.filename,
            filepath=generated_code.filepath,
            reviewed_source_code=corrected_source,
        )


code_reviewer_agent = CodeReviewerAgent()