from fastapi import FastAPI
from app.api import prompt, diff_api

app = FastAPI()

app.include_router(prompt.router)
app.include_router(diff_api.router)
