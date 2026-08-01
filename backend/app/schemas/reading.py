from datetime import datetime

from pydantic import BaseModel


class ReadingCreate(BaseModel):
    device_id: int
    temperature: float
    humidity: float
    battery: int


class ReadingResponse(BaseModel):
    id: int
    device_id: int
    temperature: float
    humidity: float
    battery: int
    created_at: datetime

    class Config:
        from_attributes = True