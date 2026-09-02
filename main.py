from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1.router import api_router

app = FastAPI()
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads",
)
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def home():
    return {
        "message": "FastAPI Inventory API is running"
    }
