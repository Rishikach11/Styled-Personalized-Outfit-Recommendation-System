from fastapi import FastAPI
from backend.app.api import auth, preferences, recommendations, feedback

app = FastAPI(title="Styled – Outfit Recommendation System")

app.include_router(auth.router, prefix="/api")
app.include_router(preferences.router, prefix="/api")
app.include_router(recommendations.router, prefix="/api")
app.include_router(feedback.router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "Backend running"}
