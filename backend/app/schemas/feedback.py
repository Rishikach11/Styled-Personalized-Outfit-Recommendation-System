from pydantic import BaseModel

class FeedbackRequest(BaseModel):
    user_id: int
    product_id: str
    action: str
