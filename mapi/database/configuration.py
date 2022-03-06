from http.client import TEMPORARY_REDIRECT
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlmodel import SQLModel, Session, create_engine
from decouple import config

from mapi.core.password import get_password_hash
from mapi.models.user import Role, UserInDB


DATABASE_URI = config("DATABASE_URI", default="sqlite:////tmp/database.db")
engine = create_engine(DATABASE_URI, echo=False)


def create_roles(session):
    try:
        admin = Role(name="admin", description="Administrator")
        visitor = Role(name="visitor", description="User")
        session.add(admin)
        session.add(visitor)
        session.commit()

    except (IntegrityError, OperationalError):
        session.rollback()
    finally:
        session.close()


def create_admin(session):
    try:
        admin = UserInDB(
            username="MrRobot",
            email="elliotalderson@protonmail.ch",
            full_name="Elliot Alderson",
            hashed_password=get_password_hash("fsociety"),
            role_name="admin",
        )
        session.add(admin)
        session.commit()

    except (IntegrityError, OperationalError):
        session.rollback()

    finally:
        session.close()


def setup_db(engine):
    try:
        SQLModel.metadata.create_all(engine)
    except OperationalError:
        print("Tables already exists")
    
    with Session(engine) as session:
        create_roles(session)
        create_admin(session)
