from pydantic import BaseModel
from datetime import datetime

class PromptRequest(BaseModel):
    user_input: str # 사용자 입력

class PromptResponse(BaseModel):
    prompt: str # 생성된 프롬프트
    timestamp: datetime
