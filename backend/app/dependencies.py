from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.device_service import DeviceService


def get_device_service(db: Session):
    return DeviceService(db)