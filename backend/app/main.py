from fastapi import FastAPI

from app.core.config import settings
from app.routers.auth import router as auth_router
from app.routers.devices import router as device_router
from app.routers.readings import router as reading_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Cloud-native IoT Device Monitoring Platform",
    version=settings.APP_VERSION,
)

# Device APIs
app.include_router(
    device_router,
    prefix="/api/v1",
)

# Authentication APIs
app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Authentication"],
)

# Sensor Reading APIs
app.include_router(
    reading_router,
    prefix="/api/v1",
)

@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "debug": settings.DEBUG,
        "status": "running",
        "message": "Welcome to CloudPulse!",
    }