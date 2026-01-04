from fastapi import APIRouter
from backend.app.schemas.feedback import FeedbackRequest

router = APIRouter()

@router.post("/feedback")
def submit_feedback(data: FeedbackRequest):
    return {"message": "Feedback recorded"}
