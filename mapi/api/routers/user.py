from typing import List
from fastapi import APIRouter, Security, Depends, HTTPException
from schemas.user import User, UserCreate
from core import security
from database.session import create_user, delete_user, get_users

router = APIRouter(prefix="/users", tags=["User"],)


@router.get("/me/", response_model=User)
async def read_users_me(current_user: User = Depends(security.get_current_active_user)):
    return current_user


@router.post("/add/")
async def register_user(
    user: UserCreate,
    current_user: User = Security(security.is_admin),
):

    status = create_user(user)
    if not status.get("ok"):
        raise HTTPException(
            status_code=409,
            detail=f"Username {user.username} is taken",
        )
    
    return status


@router.get("/", response_model=List[User])
async def get_users_in_db(current_user: User = Security(security.is_admin)):
    return get_users()


@router.post("/delete/")
async def remove_user(
    username: str, current_user: User = Security(security.is_admin)
):
    status = delete_user(username=username)
    if not status.get("ok"):
        raise HTTPException(
            status_code=409,
            detail=f"Username {username} does not exists",
        )
    return status
