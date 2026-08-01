from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.alert import AlertResponse
from app.services.alert_service import AlertService

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


@router.get(
    "",
    response_model=list[AlertResponse],
)
def get_all_alerts(
    db: Session = Depends(get_db),
):
    service = AlertService(db)

    return service.get_all_alerts()