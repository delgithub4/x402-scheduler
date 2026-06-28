from fastapi import APIRouter

from services.scheduler_service import SchedulerService

router = APIRouter(
    prefix="/scheduler",
    tags=["Scheduler"]
)

service = SchedulerService()


@router.get("/")
def scheduler():

    return service.overview()
