from contextlib import asynccontextmanager
from db import create_db_and_tables
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    create_db_and_tables()
    yield
    # Shutdown logic (if needed)
    # e.g., close connections, cleanup, etc.
