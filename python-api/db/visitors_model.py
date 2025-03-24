# db/visitors_model.py
from pydantic import BaseModel
from typing import Optional

# Define a Pydantic model for data validation
class Visitors(BaseModel):
    id: Optional[str] = None  # MongoDB ID (optional)
    name: str  # Visitor name
    visitorcount: int  # Visitor count
