from sqlalchemy.orm import Session

from app.database.models import Device


class DeviceService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_devices(self):
        return self.db.query(Device).all()

    def get_device(self, device_id: int):
        return (
            self.db.query(Device)
            .filter(Device.id == device_id)
            .first()
        )

    def create_device(self, name, status, location):
        device = Device(
            name=name,
            status=status,
            location=location,
        )

        self.db.add(device)
        self.db.commit()
        self.db.refresh(device)

        return device

    def update_device(self, device_id, name, status, location):
        device = self.get_device(device_id)

        if not device:
            return None

        device.name = name
        device.status = status
        device.location = location

        self.db.commit()
        self.db.refresh(device)

        return device

    def delete_device(self, device_id):
        device = self.get_device(device_id)

        if not device:
            return False

        self.db.delete(device)
        self.db.commit()

        return True