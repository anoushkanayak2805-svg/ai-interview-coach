from fastapi import FastAPI

app = FastAPI(
    title="InterviewIQ API",
    description="AI Interview Coach Backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to InterviewIQ 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "Server is running successfully"
    }


@app.get("/about")
def about():
    return {
        "project": "InterviewIQ",
        "version": "1.0",
        "developer": "Anoushka Nayak"
    }