from fastapi import APIRouter
from app.models.prompt_models import PromptRequest, PromptResponse
from app.services.prompt_generator import generate_prompt
from datetime import datetime

router = APIRouter()

@router.post("/generate-prompt", response_model=PromptResponse)
def generate_prompt_endpoint(request: PromptRequest):
    prompt = generate_prompt(request.user_input)
    return PromptResponse(
        prompt=prompt,
        timestamp=datetime.utcnow()
    )
