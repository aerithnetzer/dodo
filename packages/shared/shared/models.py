from datetime import datetime
from uuid import uuid4
from sqlmodel import SQLModel, Field


from typing import Optional


class ObjectMixin(SQLModel):
    attachment: Optional[str] = None
    attributed_to: Optional[str] = None
    audience: Optional[str] = None
    content: Optional[str] = None
    context: Optional[str] = None
    name: Optional[str] = None
    end_time: Optional[datetime] = None
    generator: Optional[str] = None
    icon: Optional[str] = None
    image: Optional[str] = None
    in_reply_to: Optional[str] = None
    location: Optional[str] = None
    preview: Optional[str] = None
    published: Optional[datetime] = None
    replies: Optional[str] = None
    start_time: Optional[datetime] = None
    summary: Optional[str] = None
    tag: Optional[str] = None
    updated: Optional[datetime] = None
    url: Optional[str] = None
    to: Optional[str] = None
    bto: Optional[str] = None
    cc: Optional[str] = None
    bcc: Optional[str] = None
    media_type: Optional[str] = None
    duration: Optional[str] = None


# ACTOR MODELS
class ActorBase(SQLModel):
    inbox: str = Field(default="", nullable=False)
    outbox: str = Field(default="", nullable=False)

    following: str = Field(default="", nullable=False)
    followers: str = Field(default="", nullable=False)

    preferred_username: str = Field(default="")


class Actor(ObjectMixin, table=True):
    id: str = Field(
        default_factory=lambda: str(uuid4), nullable=False, primary_key=True
    )


class ActivityBase(SQLModel):
    type: str = Field(default="Activity")
    summary: str = Field(default=None, nullable=False)
    actor: str = Field(nullable=False)
    object: str = Field(nullable=False)


class Activity(ObjectMixin, table=True):
    id: str = Field(
        default_factory=lambda: str(uuid4()), nullable=False, primary_key=True
    )
