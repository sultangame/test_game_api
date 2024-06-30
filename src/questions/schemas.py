from typing import Optional, List
from pydantic import BaseModel, Field
from src.models.questions import LevelEnum
from beanie import PydanticObjectId


class QuestionsBaseModel(BaseModel):
    question: Optional[str] = Field(max_length=1024)
    incorrect_answers: Optional[List[str]] = None
    correct_answers: Optional[List[str]] = None
    level: Optional[LevelEnum] = LevelEnum.MIDDLE


class QuestionsRead(QuestionsBaseModel):
    id: PydanticObjectId


class QuestionsEdit(QuestionsBaseModel):
    pass
