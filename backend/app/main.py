from fastapi import FastAPI
from backend.app.api import auth, preferences, recommendations, feedback
from backend.app.db.database import engine
from backend.app.db import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Styled – Outfit Recommendation System")

app.include_router(auth.router, prefix="/api")
app.include_router(preferences.router, prefix="/api")
app.include_router(recommendations.router, prefix="/api")
app.include_router(feedback.router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "Backend running"}
