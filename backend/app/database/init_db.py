from app.database.base import Base
from app.database.connection import engine
from app.database.models import Device

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")