from typing import Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None


class ApiError(BaseModel):
    success: bool
    message: str
    errors: list[str] = []
