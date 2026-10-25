
from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI Project",
    version="1.1.0"
)

@app.get("/")
async def home():
    return {"message": "My API is updated!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/about")
async def about():
    return {
        "name": "My FastAPI Project",
        "version": "1.1.0",
        "developer": "Parvej Sarkar"
    }

@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}
