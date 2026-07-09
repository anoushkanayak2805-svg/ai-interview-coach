from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.interview import router as interview_router
from app.api.answer import router as answer_router
from app.api.resume import router as resume_router

# Import both report routers
from app.api.report import (
    router as report_router,
    reports_router,
)

from app.core.exception_handlers import (
    register_exception_handlers,
)


app = FastAPI(
    title="AI Interview Coach Pro",
    description="""
Production-ready AI Interview Platform

Features

• JWT Authentication
• Resume Intelligence
• AI Interview Generation
• AI Answer Evaluation
• Hiring Report Generation

Technology Stack

• FastAPI
• PostgreSQL
• SQLAlchemy
• Alembic
• Gemini AI
• React (Frontend)
""",
    version="1.0.0",
)


# -----------------------------
# CORS
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # Local development
        "http://localhost:5173",
        "http://127.0.0.1:5173",

        # Production frontend
        "https://ai-interview-coach-gold.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Register Global Exception Handlers
# -----------------------------

register_exception_handlers(app)


# -----------------------------
# Routers
# -----------------------------

app.include_router(auth_router)

app.include_router(interview_router)

app.include_router(answer_router)

app.include_router(resume_router)

# GET /interviews/{interview_id}/report
app.include_router(report_router)

# GET /reports
app.include_router(reports_router)


# -----------------------------
# Root Endpoint
# -----------------------------

@app.get("/", tags=["Home"])
def root():
    return {
        "success": True,
        "message": "Welcome to AI Interview Coach Pro API 🚀",
        "version": "1.0.0",
    }


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "success": True,
        "status": "healthy",
        "service": "AI Interview Coach Pro",
        "version": "1.0.0",
    }