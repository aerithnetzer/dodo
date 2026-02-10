from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI, Depends
from sqlmodel import Field, SQLModel, Session
from typing import Annotated
from db import create_db_and_tables, get_session
from shared import Actor

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("uvicorn.error")

data = {123456: {"title": "Moby Dick", "author": "Herman Melville"}}


app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    create_db_and_tables()
    yield
    # Shutdown logic (if needed)
    # e.g., close connections, cleanup, etc.


SessionDep = Annotated[Session, Depends(get_session)]


def naive_search(query: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    for k in data:
        print(data[k])
        for n in data[k]:
            if query in data[k][n]:
                result.append(data[k])
            print(data[k][n])
    return result


@app.get("/works")
async def get_success() -> dict[str, str]:
    return {"status": "success!"}


@app.post("/actors/")
async def create_actor(actor: Actor, session: SessionDep) -> Actor:
    session.add(actor)
    session.commit()
    session.refresh(actor)
    return actor


@app.get("/search/works/{query}")
async def search_works(query: str) -> list[dict[str, str]]:
    return naive_search(query)


@app.get("/")
async def root():
    return {"service": "dodo-api"}
