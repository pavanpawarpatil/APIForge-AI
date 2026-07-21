from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/download",
    tags=["Download"],
)

BASE_DIR = Path("generated_projects")


@router.get("/{filename}")
def download_zip(filename: str):

    file_path = BASE_DIR / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found",
        )

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/zip",
    )