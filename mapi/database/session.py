from typing import Dict, List, Union
from decouple import config
from sqlalchemy import engine
from sqlmodel import Session, create_engine, select
from models.user import UserInDB, User
from mapi.schemas.user import UserCreate, UserUpdate
from core.password import get_password_hash


DATABASE_URL = config("DATABASE_URI", default="sqlite:///database.db")
DEBUG_MODE = config("DEBUG_STAGE", default="prod")


if DEBUG_MODE == "dev":
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
    )
else:
    engine = create_engine(
        DATABASE_URL, connect_args={"sslmode": "required"}, echo=False
    )


def get_user(username: str) -> UserInDB:

    with Session(engine) as session:

        selection = select(UserInDB).where(UserInDB.username == username)
        user = session.exec(selection).first()

    return user


def get_user_role(username: str) -> Union[str, None]:

    with Session(engine) as session:
        selection = select(UserInDB).where(UserInDB.username == username)
        user = session.exec(selection).one()

    return user.role_name


def get_users() -> List[User]:

    with Session(engine) as session:

        selection = select(UserInDB)
        users = session.exec(selection).fetchall()

    return [
        User(
            username=user.username,
            full_name=user.full_name,
            email=user.email,
            disabled=user.disabled,
            role_name=user.role_name,
        )
        for user in users
    ]


def delete_user(username: str) -> Dict[str, bool]:

    with Session(engine) as session:
        selection = select(UserInDB).where(UserInDB.username == username)
        user = session.exec(selection).first()

        if not user:
            return {"ok": False}

        session.delete(user)
        session.commit()

    return {"ok": True}


def create_user(user: UserCreate) -> Dict[str, bool]:

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


def update_user(user: UserUpdate) -> Dict[str, bool]:

    with Session(engine) as session:

        # check if user exists
        user_exists = get_user(user.username)

        if not user_exists:
            return {"ok": False}

        users_updates = user.dict(exclude_unset=True, exclude_none=True)
        users_updates.pop("username", None)
        if users_updates.pop("password", None):
            users_updates["hashed_password"] = get_password_hash(user.password)

        # update without changing memory id
        {
            setattr(user_exists, updated_field, updated_value)
            for updated_field, updated_value in users_updates.items()
        }

        session.add(user_exists)
        session.commit()
        session.refresh(user_exists)

    return {"ok": True}
