from datetime import datetime
from typing import Any
from uuid import uuid4
from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class ObjectBase(BaseModel):
    attachment: str
    attributed_to: str
    audience: str
    content: str
    context: str
    name: str
    end_time: datetime
    generator: dict
    icon: Any
    image: Any
    in_reply_to: Any
    location: Any
    preview: Any
    published: Any
    replies: Any
    start_time: datetime
    summary: str
    tag: str
    updated: datetime
    url: str
    to: str
    bto: str
    cc: str
    bcc: str
    media_type: str
    duration: str


# ACTOR MODELS
class ActorBase(SQLModel, ObjectBase):
    inbox: str = Field(default="", nullable=False)
    outbox: str = Field(default="", nullable=False)

    following: str = Field(default="", nullable=False)
    followers: str = Field(default="", nullable=False)

    preferred_username: str = Field(default="")
    pass


class Actor(ActorBase, table=True):
    id: str = Field(
        default_factory=lambda: str(uuid4), nullable=False, primary_key=True
    )


class ActivityBase(SQLModel):
    type: str = Field(default="Activity")
    summary: str = Field(default=None, nullable=False)
    actor: dict = Field(nullable=False)
    object: dict = Field(nullable=False)


class Activity(ActivityBase):
    pass
