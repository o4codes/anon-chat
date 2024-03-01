from fastapi import FastAPI

app = FastAPI(
    title="Chat API",
    description="REST API for chat",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {"message": "Server is up and running"}