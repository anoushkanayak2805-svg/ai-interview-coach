from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.interview import router as interview_router
from app.api.answer import router as answer_router

app = FastAPI(
    title="AI Interview Coach Pro"
)

app.include_router(auth_router)
app.include_router(interview_router)
app.include_router(answer_router)


@app.get("/")
def root():
    return {
        "message": "AI Interview Coach Pro API"
    }