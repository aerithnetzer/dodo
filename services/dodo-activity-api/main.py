import logging
from fastapi import FastAPI, Depends
from shared.models import Activity, Actor
from sqlmodel import Session
from typing import Annotated
from db import get_session
from lifespans import lifespan

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("uvicorn.error")

app = FastAPI(lifespan=lifespan)


SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/works")
async def get_success() -> dict[str, str]:
    return {"status": "success!"}


@app.post("/activities/")
async def create_activity(activity: Activity, session: SessionDep) -> Activity:
    session.add(activity)
    session.commit()
    session.refresh(activity)
    return activity


@app.post("/actors/")
async def create_actor(actor: Actor, session: SessionDep) -> Actor:
    session.add(actor)
    session.commit()
    session.refresh(actor)
    return actor


@app.get("/")
async def root():
    return {"service": "dodo-api"}
