from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.interview import router as interview_router
from app.api.answer import router as answer_router
from app.api.resume import router as resume_router


app = FastAPI(
    title="AI Interview Coach Pro",
    version="1.0.0",
)


# Authentication
app.include_router(auth_router)

# Interview
app.include_router(interview_router)

# Answers
app.include_router(answer_router)

# Resume
app.include_router(resume_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Interview Coach Pro API 🚀",
        "status": "running",
        "version": "1.0.0",
    }