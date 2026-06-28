from fastapi import FastAPI

from routes.scheduler import router as scheduler_router
from routes.health import router as health_router

app = FastAPI(
    title="x402-scheduler",
    version="1.0.0"
)

app.include_router(scheduler_router)
app.include_router(health_router)


@app.get("/")
def home():

    return {

        "service":"x402-scheduler",

        "status":"running"

    }
