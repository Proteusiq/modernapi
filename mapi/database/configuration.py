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

    user_1 = UserInDB(
        username="Proteusiq",
        email="praysonpi@example.com",
        full_name="Prayson W. Daniel",
        hashed_password=get_password_hash("secret"),
        disabled=False,
    )
    user_2 = UserInDB(
        username="SuperMario",
        email="supermario@example.com",
        full_name="Mario J. L. Daniel",
        hashed_password=get_password_hash("secured"),
    )

    with Session(engine) as session:

        session.add(user_1)
        session.add(user_2)
        session.commit()

    # Test:

    print("Test: Create User")
    user = get_user("Proteusiq")

    print("Results:")
    print(user)
