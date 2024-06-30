from typing import Optional, List
from beanie import Document
from pydantic import Field
from enum import Enum


class LevelEnum(Enum):
    BEGINNER = "BEGINNER"
    MIDDLE = "MIDDLE"
    SENIOR = "SENIOR"


class QuestionODM(Document):
    question: Optional[str] = Field(max_length=1024)
    incorrect_answers: Optional[List[str]] = None
    correct_answers: Optional[List[str]] = None
    subject: Optional[str] = None
    theme: Optional[str] = None
    level: Optional[LevelEnum] = LevelEnum.MIDDLE

    class Config:
        json_shema_extra = {
            "example": {
                "question": "String of required field question",
                "incorrect_answers": "List of incorrect answers",
                "correct_answers": "List of correct answers",
                "subject": "string",
                "theme": "string",
                "level": LevelEnum.MIDDLE
            }
        }

    class Settings:
        name = "questions"
