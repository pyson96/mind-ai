from fastapi import APIRouter
from app.models.diff_models import DiffRequest, DiffResponse
from app.services.diff_service import calculate_diff
from datetime import datetime

router = APIRouter()

@router.post("/save-diff", response_model=DiffResponse)
def save_diff(request: DiffRequest):
    diffs = calculate_diff(request.before, request.after)
    return DiffResponse(
        diff=diffs,
        timestamp=datetime.utcnow()
    )
