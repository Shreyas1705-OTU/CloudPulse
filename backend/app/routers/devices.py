from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.device import DeviceCreate, DeviceResponse
from app.services.device_service import DeviceService

router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


@router.get("/", response_model=list[DeviceResponse])
def get_devices(db: Session = Depends(get_db)):
    service = DeviceService(db)
    return service.get_all_devices()


@router.get("/{device_id}", response_model=DeviceResponse)
def get_device(device_id: int, db: Session = Depends(get_db)):
    service = DeviceService(db)

    device = service.get_device(device_id)

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return device


@router.post("/", response_model=DeviceResponse, status_code=201)
def create_device(
    device: DeviceCreate,
    db: Session = Depends(get_db)
):
    service = DeviceService(db)

    return service.create_device(
        name=device.name,
        status=device.status,
        location=device.location,
    )


@router.put("/{device_id}", response_model=DeviceResponse)
def update_device(
    device_id: int,
    device: DeviceCreate,
    db: Session = Depends(get_db)
):
    service = DeviceService(db)

    updated_device = service.update_device(
        device_id=device_id,
        name=device.name,
        status=device.status,
        location=device.location,
    )

    if not updated_device:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return updated_device


@router.delete("/{device_id}")
def delete_device(
    device_id: int,
    db: Session = Depends(get_db)
):
    service = DeviceService(db)

    success = service.delete_device(device_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return {
        "message": "Device deleted successfully"
    }