import ast

from app.schemas.validation import ValidationResult


class ValidationService:
    """
    Validates generated Python source code.
    """

    def validate_syntax(
        self,
        source_code: str,
    ) -> list[str]:

        errors = []

        try:
            ast.parse(source_code)

        except SyntaxError as e:
            errors.append(
                f"SyntaxError: {e.msg} (line {e.lineno})"
            )

        return errors

    def validate_imports(
        self,
        source_code: str,
    ) -> list[str]:
        """
        Placeholder for future import validation.
        """

        return []

    def validate(
        self,
        source_code: str,
    ) -> ValidationResult:

        syntax_errors = self.validate_syntax(
            source_code
        )

        import_errors = self.validate_imports(
            source_code
        )

        return ValidationResult(
            valid=(
                not syntax_errors
                and not import_errors
            ),
            syntax_errors=syntax_errors,
            import_errors=import_errors,
        )


validation_service = ValidationService()