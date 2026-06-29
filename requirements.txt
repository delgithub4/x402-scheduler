from typing import Any

from pydantic import BaseModel


class JobRequest(BaseModel):
    job_name: str
    schedule: str
    payload: dict[str, Any] = {}


class JobResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None
