import os

from sqlmodel import SQLModel, Session, create_engine

postgres_url = os.getenv(
    "DATABASE_URL", "postgresql://devuser:devpass@localhost:5432/dodo"
)

engine = create_engine(postgres_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
