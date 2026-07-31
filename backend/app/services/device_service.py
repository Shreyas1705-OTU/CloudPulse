from fastapi import HTTPException

from app.core.logger import logger
from app.schemas.device import Device


DEVICES = [
    Device(
        id=1,
        name="Temperature Sensor",
        status="Online",
        location="Warehouse A"
    ),
    Device(
        id=2,
        name="Pressure Sensor",
        status="Offline",
        location="Warehouse B"
    ),
    Device(
        id=3,
        name="Gateway Device",
        status="Online",
        location="Main Office"
    )
]


def get_all_devices():
    logger.info("Returning all devices")
    return DEVICES


def get_device_by_id(device_id: int):
    for device in DEVICES:
        if device.id == device_id:
            logger.info(f"Returning device with ID {device_id}")
            return device

    logger.error(f"Device with ID {device_id} not found")

    raise HTTPException(
        status_code=404,
        detail="Device not found"
    )