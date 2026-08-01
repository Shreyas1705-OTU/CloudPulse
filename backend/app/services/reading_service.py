from sqlalchemy.orm import Session

from app.database.models import Reading
from app.services.alert_service import AlertService


class ReadingService:

    def __init__(self, db: Session):
        self.db = db

    def create_reading(
        self,
        device_id: int,
        temperature: float,
        humidity: float,
        battery: int,
    ):
        reading = Reading(
            device_id=device_id,
            temperature=temperature,
            humidity=humidity,
            battery=battery,
        )

        self.db.add(reading)
        self.db.commit()
        self.db.refresh(reading)

        alert_service = AlertService(self.db)

        if temperature > 35:
            alert_service.create_alert(
                device_id=device_id,
                message="High temperature detected",
                severity="HIGH",
            )

        if humidity < 20:
            alert_service.create_alert(
                device_id=device_id,
                message="Low humidity detected",
                severity="MEDIUM",
            )

        if battery < 20:
            alert_service.create_alert(
                device_id=device_id,
                message="Low battery detected",
                severity="HIGH",
            )

        return reading

    def get_all_readings(self):
        return (
            self.db.query(Reading)
            .order_by(Reading.created_at.desc())
            .all()
        )

    def get_readings_for_device(
        self,
        device_id: int,
    ):
        return (
            self.db.query(Reading)
            .filter(Reading.device_id == device_id)
            .order_by(Reading.created_at.desc())
            .all()
        )