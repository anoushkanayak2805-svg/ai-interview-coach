from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.interview import router as interview_router
from app.api.answer import router as answer_router

from app.core.config import settings

print("=" * 60)
print(settings.DATABASE_URL)
print("=" * 60)

from sqlalchemy import text
from app.database import engine

with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'interview_sessions'
        ORDER BY ordinal_position
    """))

    print("\n===== SQLAlchemy sees these columns =====")
    for row in result:
        print(row[0])
    print("=========================================\n")

app = FastAPI(
    title="AI Interview Coach API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(interview_router)
app.include_router(answer_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Interview Coach Pro 🚀",
        "status": "running"
    }
