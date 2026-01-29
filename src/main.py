# libraries import
from fastapi import FastAPI

# files import
from routes import base


app = FastAPI()

app.include_router(base.base_router)
# app.include_router(qa.router)

