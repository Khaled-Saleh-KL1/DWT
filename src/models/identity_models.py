from pydantic import BaseModel

# Input
class IdentityRequest(BaseModel):
    base64_image: str

# output
class IdentityResponse(BaseModel):
    full_name_Arabic: str | None = None
    full_name_English: str | None = None
    national_number: str | None = None
    gender: str | None = None
    date_of_birth: str | None = None
    born_place: str | None = None
    mother_name: str | None = None