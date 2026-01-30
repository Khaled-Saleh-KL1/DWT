# libraries import
from fastapi import APIRouter
import json

# files import
from models import IdentityRequest, IdentityResponse
from stores import OCRService
from stores import llm_service

identity_router = APIRouter()

ocr_service = OCRService()

def parse_llm_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)

@identity_router.post("/extract", response_model=IdentityResponse)
def extract_identity(request: IdentityRequest):
    raw_text = ocr_service.extract_text(request.base64_image)

    if not raw_text:
        return IdentityResponse # empty

    prompt = f"""
    Below is raw text extracted from an ID card OCR.
    Extract the following details into a strict JSON format: full_name_Arabic, full_name_English, national_number, gender, date_of_birth, born_place, mother_name.
    If a field is missing, return null. Do not say anything else, just the JSON.

    Raw Text:
    {raw_text}
    """

    llm_service_response = llm_service.generate_answer(
        question=prompt,
        context="You are a data extraction assistant."
    )

    try:
        data = parse_llm_json(llm_service_response)
        return IdentityResponse(**data)
    except Exception:
        return IdentityResponse()