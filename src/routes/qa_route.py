# libraries import
from fastapi import APIRouter

# files import
from stores import QAStore, LLMService
from models import InputData, QuestionRequest, AnswerResponse


qa_router = APIRouter()

qa_store = QAStore()
llm_service = LLMService()

@qa_router.post("/add-data")
def add_data(request: InputData):
    qa_store.save_context(request.content)
    return {"message": "Data added successfully"}

@qa_router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    context = qa_store.get_context()

    if not context:
        return AnswerResponse(answer="No context loaded.")

    answer = llm_service.generate_answer(request.question, context)
    return AnswerResponse(answer=answer)
