from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.session import get_db
from app.schemas.reading import (
    ReadingCreate,
    ReadingResponse,
)
from app.services.reading_service import ReadingService

router = APIRouter(
    prefix="/readings",
    tags=["Readings"],
)


@router.post(
    "",
    response_model=ReadingResponse,
    status_code=201,
)
def create_reading(
    reading: ReadingCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = ReadingService(db)

    return service.create_reading(
        device_id=reading.device_id,
        temperature=reading.temperature,
        humidity=reading.humidity,
        battery=reading.battery,
    )


@router.get(
    "",
    response_model=list[ReadingResponse],
)
def get_all_readings(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = ReadingService(db)

    return service.get_all_readings()


@router.get(
    "/device/{device_id}",
    response_model=list[ReadingResponse],
)
def get_device_readings(
    device_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = ReadingService(db)

    return service.get_readings_for_device(
        device_id
    )