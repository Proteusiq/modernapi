from sqlmodel import SQLModel, create_engine
from decouple import config
from api.security import get_password_hash


DATABASE_URL = config("DATABASE_URI", default="sqlite:///database.db")
engine = create_engine(DATABASE_URL, echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    from sqlmodel import Session, select
    from models.user import UserInDB
    from database.session import get_user

    create_db_and_tables()

    hero_1 = UserInDB(
        username="Deadpond",
        email="deadpond@example.com",
        full_name="Dive Wilson",
        hashed_password=get_password_hash("secret"),
        disabled=True,
    )
    hero_2 = UserInDB(
        username="Spider-Boy",
        email="spider@example.com",
        full_name="Pedro Parqueador",
        hashed_password=get_password_hash("secured"),
    )

    with Session(engine) as session:

        session.add(hero_1)
        session.add(hero_2)
        session.commit()

    # Test:

    print("Test:")
    user = get_user("Spider-Boy")

    print("Results:")
    print(user)
