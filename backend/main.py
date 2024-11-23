from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import Settings

settings = Settings()
app = FastAPI(title="FastAPI React App", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
