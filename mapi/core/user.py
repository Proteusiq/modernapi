from sqlmodel import Session

from fastapi import HTTPException, status
from core.security import get_password_hash
from models.user import UserInDB, User


def create(request: UserInDB, db: Session):
    hashedPassword = get_password_hash(request.password)
    user = UserInDB(
        username=request.username, email=request.email, password=hashedPassword
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def show(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"User with username {username} not found"
        )
    return user


def get_all(db: Session):
    return db.query(User).all()
