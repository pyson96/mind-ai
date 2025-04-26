from fastapi import FastAPI
from app.api import prompt

app = FastAPI()

# 라우터 등록
app.include_router(prompt.router)
