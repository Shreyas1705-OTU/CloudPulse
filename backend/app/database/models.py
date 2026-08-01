from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime,
)
from sqlalchemy.sql import func

from app.database.base import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(20),
        default="user",
        nullable=False
    )


class Reading(Base):
    __tablename__ = "readings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    device_id = Column(
        Integer,
        ForeignKey("devices.id"),
        nullable=False
    )

    temperature = Column(
        Float,
        nullable=False
    )

    humidity = Column(
        Float,
        nullable=False
    )

    battery = Column(
        Integer,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    
class Alert(Base):
    __tablename__ = "alerts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    device_id = Column(
        Integer,
        ForeignKey("devices.id"),
        nullable=False
    )

    message = Column(
        String(255),
        nullable=False
    )

    severity = Column(
        String(20),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )