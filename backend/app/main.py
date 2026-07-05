from fastapi import FastAPI
from backend.app.api.repository import router as repository_router

app = FastAPI(
    title="CodePilot AI",
    version="1.0.0"
)

app.include_router(repository_router, prefix="/repository", tags=["Repository"])


@app.get("/")
def root():
    return {"message": "Welcome to CodePilot AI 🚀"}


@app.get("/health")
def health():
    return {"status": "healthy"}