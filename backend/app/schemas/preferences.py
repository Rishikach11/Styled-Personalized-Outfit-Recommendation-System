from pydantic import BaseModel
from typing import List

class PreferenceRequest(BaseModel):
    user_id: int
    preferred_colors: List[str]
    preferred_style: str
