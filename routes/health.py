from fastapi import APIRouter

from core.config import settings
from core.responses import success

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
async def health():

    return success(
        message="Health check successful.",
        data={
            "status": "healthy",
            "service": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT,
        },
    )
