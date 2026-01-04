from fastapi import APIRouter
from backend.app.schemas.auth import RegisterRequest, LoginRequest

router = APIRouter()

@router.post("/register")
def register(data: RegisterRequest):
    return {"message": "User registered"}

@router.post("/login")
def login(data: LoginRequest):
    return {
        "token": "dummy-jwt-token",
        "user_id": 1,
        "has_preferences": False
    }
