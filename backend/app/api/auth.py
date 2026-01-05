from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.auth import RegisterRequest, LoginRequest
from backend.app.schemas.auth import RegisterRequest, LoginRequest
from backend.app.db.database import get_db
from backend.app.db.models import User
from backend.app.core.security import hash_password

from backend.app.schemas.auth import LoginRequest
from backend.app.db.database import get_db
from backend.app.db.models import User
from backend.app.core.security import verify_password, create_access_token


router = APIRouter()

@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=data.email,
        password_hash=hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User registered successfully"}

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)})

    return {
        "token": token,
        "user_id": user.id
    }
