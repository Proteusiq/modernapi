from typing import Optional
from decouple import config
from sqlmodel import Field, Session, SQLModel, create_engine


DATABASE_URL = config("DATABASE_URI", default="sqlite:///database.db")

engine = create_engine(DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)


def get_db():

    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
