from pydantic import BaseModel
from typing import Optional


class Answer(BaseModel):
    answer: Optional[str] = None
