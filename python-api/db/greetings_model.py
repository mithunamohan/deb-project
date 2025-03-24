# db/greetings_model.py
from pydantic import BaseModel
from typing import Optional

# Define a Pydantic model for data validation
class Greetings(BaseModel):
    id: Optional[str] = None  # MongoDB ID (optional)
    greetings: str  # Greeting message
