from decouple import config
from sqlmodel import Session, create_engine, select
from models.user import UserInDB


DATABASE_URL = config("DATABASE_URI", default="sqlite:///database.db")
engine = create_engine(DATABASE_URL, echo=False)


def get_user(username: str):

    with Session(engine) as session:

        selection = select(UserInDB).where(UserInDB.username == username)
        user = session.exec(selection).first()

        return user


def yield_session():

    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
