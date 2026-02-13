import logging
from fastapi import FastAPI, Depends, HTTPException
from shared.models import Activity, Actor, Collection, Object, CollectionObjectLink
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


@app.post("/following/")
async def post_following(session: SessionDep) -> Activity:
    return Activity(
        actor_id="current actor",
        object_id="",
    )


@app.get("/activities/{id}")
async def get_activity(session: SessionDep) -> Activity:
    return Activity(
        actor_id="",
        object_id="",
    )


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


@app.get("/collections/{collection}")
async def get_collection() -> Collection:
    return Collection()


@app.post("/objects/")
async def post_objects(
    object: Object,
    session: SessionDep,
    token: Annotated[str, Depends(oauth2_scheme)],
) -> dict[str, str | Object]:
    session.add(object)
    session.commit()
    session.refresh(object)
    return {"token": token, "object": object}


@app.post("/collections/")
async def post_collections(
    collection: Collection,
    session: SessionDep,
    token: Annotated[str, Depends(oauth2_scheme)],
) -> dict[str, str | Collection]:
    session.add(collection)
    session.commit()
    session.refresh(collection)
    return {"token": token, "collection": collection}


@app.post("/collections/{collection_id}/{object_id}")
async def post_object_to_collection(
    collection_id: str,
    object_id: str,
    session: SessionDep,
) -> None:
    collection = session.get(Collection, collection_id)
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")

    obj = session.get(Object, object_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Object not found")

    link = CollectionObjectLink(
        collection_id=collection_id,
        object_id=object_id,
    )

    session.add(link)
    session.commit()


@app.get("/")
async def root():
    return {"service": "dodo-api"}
