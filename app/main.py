from fastapi import FastAPI
from sqlmodel import SQLModel
from sqlalchemy.exc import OperationalError
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware

from .routers import books




app = FastAPI(
    title="Library Management System",
    description="Simple Library CRUD API using FastAPI and PostgreSQL",
    version="1.0.0",
)


@app.on_event("startup")
def on_startup():
    try:
        SQLModel.metadata.create_all(engine)
        print("Database Connected Successfully!")
    except OperationalError as e:
        print("Database Connection Failed:", e)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include book routes
app.include_router(books.router)


@app.get("/")
def root():
    return {
        "message": "Library Management API is running"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
