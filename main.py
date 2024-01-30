
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import recognition_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(prefix="/api",router=recognition_route.router)

    
    

