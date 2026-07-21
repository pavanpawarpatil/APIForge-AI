from fastapi import APIRouter

from app.schemas.generator import (
    GenerateRequest,
    GenerateResponse,
)

from app.services.generator_service import GeneratorService

router = APIRouter(
    prefix="/generate",
    tags=["AI Generator"],
)


@router.post(
    "/",
    response_model=GenerateResponse,
)
def generate_backend(request: GenerateRequest):

    return GeneratorService.generate_backend(request)