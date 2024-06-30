from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.config import settings
from src.api import api_v1
from fastapi import FastAPI
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    await settings.initial_database()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="system of lms testing your skills api",
    version="0.0.1",
    openapi_tags=[{"name": "Testing yourself"}],
    debug=settings.DEBUG
)
origins = [
    "http://localhost:3000/",
    "http://localhost:5432/",
    "http://localhost:7000/"
]

app.include_router(api_v1)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization"
    ],
)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=settings.RELOAD, host=settings.HOST, port=settings.PORT)
