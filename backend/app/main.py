from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI(
    title="CloudPulse API",
    description="Cloud-native IoT Device Monitoring Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "application": "CloudPulse",
        "status": "running",
        "message": "Welcome to CloudPulse!"
    }