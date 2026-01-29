# libraries import
from fastapi import APIRouter, Depends

# files import
from helpers import get_settings, Settings


qa_router = APIRouter(
    prefix="/llm/v1"
)

