from fastapi import FastAPI

from app.db.database import engine

app = FastAPI()

@app.get("/health")
def health():
    return {
        "database": str(engine.url)
    }