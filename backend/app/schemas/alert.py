from datetime import datetime

from pydantic import BaseModel


class AlertCreate(BaseModel):
    device_id: int
    message: str
    severity: str


class AlertResponse(BaseModel):
    id: int
    device_id: int
    message: str
    severity: str
    created_at: datetime

    class Config:
        from_attributes = True