
from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI Project",
    description="My first deployed FastAPI application",
    version="1.0.0",
)


@app.get("/")
async def home():
    return {"message": "Hello, my name is alxsa"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
