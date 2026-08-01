from app.database.connection import SessionLocal
from app.database.models import Device

db = SessionLocal()

devices = [
    Device(
        name="Temperature Sensor",
        status="Online",
        location="Warehouse A"
    ),
    Device(
        name="Pressure Sensor",
        status="Offline",
        location="Warehouse B"
    ),
    Device(
        name="Gateway Device",
        status="Online",
        location="Main Office"
    ),
]

db.add_all(devices)
db.commit()

print("Database seeded successfully!")

db.close()