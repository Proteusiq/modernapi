from sqlmodel import Session, select
from models.user import UserInDB
from database.configuration import engine


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
