from sqlalchemy.orm import Session

from app.core.metrics import (
    READINGS_TOTAL,
    ALERTS_TOTAL,
    TEMPERATURE_GAUGE,
    HUMIDITY_GAUGE,
    BATTERY_GAUGE,
)
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

        # -----------------------------
        # Update Prometheus Metrics
        # -----------------------------
        READINGS_TOTAL.inc()
        TEMPERATURE_GAUGE.set(temperature)
        HUMIDITY_GAUGE.set(humidity)
        BATTERY_GAUGE.set(battery)

        alert_service = AlertService(self.db)

        if temperature > 35:
            alert_service.create_alert(
                device_id=device_id,
                message="High temperature detected",
                severity="HIGH",
            )
            ALERTS_TOTAL.inc()

        if humidity < 20:
            alert_service.create_alert(
                device_id=device_id,
                message="Low humidity detected",
                severity="MEDIUM",
            )
            ALERTS_TOTAL.inc()

        if battery < 20:
            alert_service.create_alert(
                device_id=device_id,
                message="Low battery detected",
                severity="HIGH",
            )
            ALERTS_TOTAL.inc()

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