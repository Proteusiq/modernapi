from sqlmodel import SQLModel, create_engine
from decouple import config
from core.security import get_password_hash


DATABASE_URL = config("DATABASE_URI", default="sqlite:///database.db")
engine = create_engine(DATABASE_URL, echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    from sqlmodel import Session, select
    from models.user import UserInDB
    from database.session import get_user

    create_db_and_tables()

    mrrobot = UserInDB(
        username="MrRobot",
        email="elliotalderson@protonmail.ch",
        full_name="Elliot Alderson",
        hashed_password=get_password_hash("fsociety"),
        disabled=False,
        access_level=5,
    )


    with Session(engine) as session:

        session.add(mrrobot)
        session.commit()

        print(f"[+]  Created {mrrobot.username!r}")

    # Test:

    print(f"[+]  Retrieve {mrrobot.username!r}")
    user = get_user(mrrobot.username)

    print((f"User {user.full_name!r} with "
           f"access level {user.access_level!r} "
           "was added")
    )
