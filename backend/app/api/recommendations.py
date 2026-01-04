from fastapi import APIRouter
from backend.app.schemas.recommendation import RecommendationRequest

router = APIRouter()

@router.post("/recommendations")
def get_recommendations(data: RecommendationRequest):
    return {
        "outfits": [
            {
                "items": [
                    {
                        "product_id": "D1",
                        "image_url": "https://dummyimage.com/300",
                        "category": "dress"
                    }
                ],
                "reason": "Matches your formal red preference"
            }
        ]
    }
