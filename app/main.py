from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)


@app.get("/")
def root():
    return {
        "message": "AI Code Assist Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }