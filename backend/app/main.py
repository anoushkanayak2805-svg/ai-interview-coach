from fastapi import FastAPI

from app.database import Base, engine
from app.api.auth import router as auth_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Interview Coach API")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "AI Interview Coach API"}