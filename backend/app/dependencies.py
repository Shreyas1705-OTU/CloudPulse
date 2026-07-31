from app.services import device_service


def get_device_service():
    """
    Returns the device service.

    Later this function will return a database-backed
    service instance.
    """

    return device_service