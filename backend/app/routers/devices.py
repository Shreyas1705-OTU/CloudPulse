from fastapi import APIRouter, Depends

from app.dependencies import get_device_service
from app.schemas.device import Device

router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)


@router.get("/", response_model=list[Device])
def get_devices(service=Depends(get_device_service)):
    return service.get_all_devices()


@router.get("/{device_id}", response_model=Device)
def get_device(
    device_id: int,
    service=Depends(get_device_service)
):
    return service.get_device_by_id(device_id)