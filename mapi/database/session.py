from typing import Dict, Literal
from decouple import config
from sqlmodel import Session, create_engine, select
from models.user import UserInDB, User
from schemas.user import UserCreate
from core.password import get_password_hash


def get_connection(mode:Literal["dev", "prod"]="prod") -> Session:

    DATABASE_URL = config("DATABASE_URI", default="sqlite:///database.db")
    if mode == "dev":
        return create_engine(DATABASE_URL, echo=True)
    return create_engine(DATABASE_URL,  connect_args={"sslmode": "required"}, echo=False)


def get_user(username: str) -> UserInDB:

    engine = get_connection(mode=config("DEBUG_STAGE", default="prod"))
    with Session(engine) as session:

        selection = select(UserInDB).where(UserInDB.username == username)
        user = session.exec(selection).first()

        return user


def get_users() -> User:

    engine = get_connection(mode=config("DEBUG_STAGE", default="prod"))
    with Session(engine) as session:

        selection = select(User)
        users = session.exec(selection)

        return users


def delete_user(username: str) -> Dict[str, bool]:
    engine = get_connection(mode=config("DEBUG_STAGE", default="prod"))
    with Session(engine) as session:
        selection = select(UserInDB).where(UserInDB.username == username
        )
        user = session.exec(selection).first()

        if not user:
            return {"ok": False}

        session.delete(user)
        session.commit()
        return {"ok": True}



def create_user(user: UserCreate) -> Dict[str, bool]:
    engine = get_connection(mode=config("DEBUG_STAGE", default="prod"))
    with Session(engine) as session:

        # check if user exists
        user_exists = get_user(user.username)

        if user_exists:
            return {"ok": False}

        user_created = UserInDB(
            username=user.username,
            email=user.email,
            hashed_password=get_password_hash(user.password),
            full_name=user.full_name,
            role_name=user.role_name,
        )
        session.add(user_created)
        session.commit()
        session.refresh(user_created)

    return {"ok": True}

