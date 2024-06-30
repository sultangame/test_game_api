from fastapi import APIRouter
from .questions import question_router


api_v1 = APIRouter(
    prefix="/api/v1"
)
api_v1.include_router(question_router)