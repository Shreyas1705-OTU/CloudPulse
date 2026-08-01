from sqlalchemy.orm import Session

from app.database.models import Reading


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