from sqlmodel import Session

from fastapi import HTTPException, status
from schema.hash import Hash


def create(request: User, db: Session):
    hashedPassword = Hash.bcrypt(request.password)
    user = User(name=request.name, email=request.email, password=hashedPassword)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def show(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return user


def get_all(db: Session):
    return db.query(models.User).all()
