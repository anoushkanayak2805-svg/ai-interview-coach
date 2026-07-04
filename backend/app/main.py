from fastapi import FastAPI

from app.database.connection import engine

from app.database.base import Base

from app.models.user import User

app = FastAPI(
    title="InterviewIQ API",
    version="1.0.0"
)


Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "InterviewIQ Backend Running 🚀"
    }