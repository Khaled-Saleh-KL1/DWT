from pydantic import BaseModel

# Endpoint 1
class InputData(BaseModel):
    content: str

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
