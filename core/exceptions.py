from fastapi import FastAPI, Request

from core.logging_config import logger
from core.responses import error


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ):
        logger.exception(exc)

        return error(
            message="Internal Server Error",
            errors=[str(exc)],
            status_code=500,
        )
