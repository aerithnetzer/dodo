import logging
from fastapi import FastAPI, Depends
from shared.models import Activity, Actor
from sqlmodel import Session
from typing import Annotated
from db import get_session
from lifespans import lifespan
from fastapi.security import OAuth2PasswordBearer

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("uvicorn.error")

app = FastAPI(lifespan=lifespan)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/activities/{id}")
async def get_activity(session: SessionDep) -> Activity:
    return Activity(actor="", object="")


@app.post("/activities/")
async def post_activity(
    activity: Activity,
    session: SessionDep,
    token: Annotated[str, Depends(oauth2_scheme)],
) -> dict[str, str | Activity]:
    return {"token": token, "activity": activity}


@app.post("/actors/")
async def create_actor(actor: Actor, session: SessionDep) -> Actor:
    session.add(actor)
    session.commit()
    session.refresh(actor)
    return actor


@app.get("/")
async def root():
    return {"service": "dodo-api"}
