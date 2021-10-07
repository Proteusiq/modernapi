from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select


class User(SQLModel, table=True):
    username: Optional[str] = Field(default=None, primary_key=True)
    email: str
    full_name: str
    disabled: Optional[bool] = None


class UserInDB(SQLModel, table=True):
    username: Optional[str] = Field(default=None, primary_key=True)
    email: str
    full_name: str
    disabled: Optional[bool] = None
    hashed_password: str


hero_1 = UserInDB(
    username="Deadpond",
    email="deadpond@example.com",
    full_name="Dive Wilson",
    hashed_password="gogo",
)
hero_2 = UserInDB(
    username="Spider-Boy",
    email="spider@example.com",
    full_name="Pedro Parqueador",
    hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
)


engine = create_engine("sqlite:///database.db")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()

# with Session(engine) as session:

#     session.add(hero_1)
#     session.add(hero_2)
#     session.commit()

with Session(engine) as session:

    selection = select(UserInDB).where(UserInDB.username == "Spider-Boy")
    result = session.exec(selection).first()

    print(result)


def get_user(username: str):

    with Session(engine) as session:

        selection = select(UserInDB).where(UserInDB.username == username)
        user = session.exec(selection).first()

        return user
