# Import the huggingface token
import os
from helpers import get_settings
settings = get_settings()
os.environ["HF_TOKEN"] = settings.HF_TOKEN

# libraries import
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# files import
from routes import base
from routes import qa_route
from routes import identity_route

app = FastAPI()

app.include_router(base.base_router)
app.include_router(qa_route.qa_router)
app.include_router(identity_route.identity_router)

app.mount("/GUI", StaticFiles(directory="views", html=True), name="static")
