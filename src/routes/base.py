# libraries import
from fastapi import APIRouter, Depends

# files import
from helpers import get_settings, Settings


base_router = APIRouter()

@base_router.get("/")
def welcome(app_settings: Settings = Depends(get_settings)):
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION

    return {
        "Message": f"Hello, Welcome to {app_name} version {app_version}"
    }
