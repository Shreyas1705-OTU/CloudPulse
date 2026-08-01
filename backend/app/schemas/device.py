from pydantic import BaseModel, ConfigDict


class DeviceCreate(BaseModel):
    name: str
    status: str
    location: str


class DeviceResponse(BaseModel):
    id: int
    name: str
    status: str
    location: str

    model_config = ConfigDict(from_attributes=True)