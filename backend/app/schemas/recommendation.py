from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    user_id: int
    occasion: str
