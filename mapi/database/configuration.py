from sqlmodel import SQLModel, create_engine
from decouple import config

DATABASE_URL = config("DATABASE_URI", default="sqlite:///database.db")
engine = create_engine(DATABASE_URL, echo=True)


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
        hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        disabled=True,
    )
    hero_2 = UserInDB(
        username="Spider-Boy",
        email="spider@example.com",
        full_name="Pedro Parqueador",
        hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
    )

    with Session(engine) as session:

        session.add(hero_1)
        session.add(hero_2)
        session.commit()

    # Test:
    user = get_user("Spider-Boy")
    print(user)
