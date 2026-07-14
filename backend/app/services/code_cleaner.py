import re


class CodeCleaner:
    """
    Cleans LLM-generated source code.
    """

    def clean(self, source_code: str) -> str:
        source_code = source_code.strip()

        # Remove opening code fence
        source_code = re.sub(
            r"^```(?:python|py)?\s*\n",
            "",
            source_code,
            flags=re.IGNORECASE,
        )

        # Remove closing code fence
        source_code = re.sub(
            r"\n```$",
            "",
            source_code,
        )

        return source_code.strip()


code_cleaner = CodeCleaner()