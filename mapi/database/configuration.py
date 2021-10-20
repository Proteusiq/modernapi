from sqlmodel import SQLModel, create_engine
from decouple import config



DATABASE_URL = config("DATABASE_URI", default="sqlite:///database.db")
engine = create_engine(DATABASE_URL, echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    from schemas.user import UserCreate
    from database.session import get_user, create_user

    create_db_and_tables()

    admin = UserCreate(
        username="MrRobot",
        email="elliotalderson@protonmail.ch",
        full_name="Elliot Alderson",
        password="fsociety",
        disabled=False,
        role_name="admin",
    )

    
    create_user(user=admin)
    print(f"[+]  Created {admin.username!r}")

    # Test:

    print(f"[+]  Retrieve {admin.username!r}")
    user = get_user(admin.username)

    print((f"User {user.full_name!r} added to DB"))
