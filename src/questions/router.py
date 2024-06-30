from .schemas import QuestionsRead, QuestionsEdit
from beanie import PydanticObjectId
from src.models import QuestionODM
from src.crud import DatabaseCRUD
from fastapi import APIRouter
from typing import List, Optional


questions_crud = DatabaseCRUD(QuestionODM)

question_router = APIRouter(
    prefix="/questions",
    tags=["questions"]
)


@question_router.get(
    "/get/all/questions/",
    response_model=List[QuestionsRead]
)
async def get_all_questions():
    answer = await questions_crud.find_all()
    return answer


@question_router.get("/get/filtered/questions/")
async def get_questions_filtered(subject: str, theme: Optional[str] = None):
    if theme is None:
        question_filter: dict = {"subject": subject}
    else:
        question_filter: dict = {"subject": subject, "theme": theme}
    answer = await questions_crud.find_filtered(filter_document=question_filter)
    return answer


@question_router.get(
    "/get/one/{_id}/question/",
    response_model=QuestionsRead
)
async def get_one_question(
        _id: PydanticObjectId
):
    answer = await questions_crud.find_one(_id=_id)
    return answer


@question_router.post(
    "/add/new/question/",
    response_model=QuestionsRead
)
async def add_new_question(document: QuestionODM):
    answer = await questions_crud.add_one(document=document)
    return answer


@question_router.delete(
    "/delete/one/{_id}/question/"
)
async def delete_one_question(_id: PydanticObjectId):
    result = await questions_crud.delete_document(_id=_id)
    return result


@question_router.patch("/edit/one/{_id}/question/")
async def edit_one_question(_id: PydanticObjectId, body: QuestionsEdit):
    answer = await questions_crud.edit_document(_id=_id, body=body)
    return answer
