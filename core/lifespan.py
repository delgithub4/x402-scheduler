from contextlib import asynccontextmanager

from core.logging_config import logger


@asynccontextmanager
async def lifespan(app):

    logger.info("=" * 60)
    logger.info("%s starting...", app.title)
    logger.info("Application ready.")
    logger.info("=" * 60)

    yield

    logger.info("=" * 60)
    logger.info("%s shutting down...", app.title)
    logger.info("=" * 60)
