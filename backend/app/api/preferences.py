from fastapi import APIRouter
from backend.app.schemas.preferences import PreferenceRequest

router = APIRouter()

@router.post("/preferences")
def save_preferences(data: PreferenceRequest):
    return {"message": "Preferences saved"}
