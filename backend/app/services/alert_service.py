from sqlalchemy.orm import Session

from app.database.models import Alert


class AlertService:

    def __init__(self, db: Session):
        self.db = db

    def create_alert(
        self,
        device_id: int,
        message: str,
        severity: str,
    ):
        alert = Alert(
            device_id=device_id,
            message=message,
            severity=severity,
        )

        self.db.add(alert)
        self.db.commit()
        self.db.refresh(alert)

        return alert

    def get_all_alerts(self):
        return (
            self.db.query(Alert)
            .order_by(Alert.created_at.desc())
            .all()
        )

    def get_alerts_for_device(
        self,
        device_id: int,
    ):
        return (
            self.db.query(Alert)
            .filter(Alert.device_id == device_id)
            .order_by(Alert.created_at.desc())
            .all()
        )