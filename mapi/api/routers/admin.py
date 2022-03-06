from typing import List
from fastapi import APIRouter, Security, HTTPException
from mapi.schemas.user import User, UserCreate, UserUpdate
from mapi.core import security
from mapi.database.session import create_user, delete_user, get_users, update_user

router = APIRouter(
    prefix="/admin",
    tags=["administrator"],
)


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


@router.patch("/update/")
async def update_user_in_db(
    user: UserUpdate,
    current_user: User = Security(security.is_admin),
):

    status = update_user(user)
    if not status.get("ok"):
        raise HTTPException(
            status_code=409,
            detail=f"Username {user.username} does not exist",
        )

    return status


@router.get("/show/", response_model=List[User])
async def get_users_in_db(current_user: User = Security(security.is_admin)):
    return get_users()


@router.delete("/delete/")
async def remove_user(username: str, current_user: User = Security(security.is_admin)):
    status = delete_user(username=username)
    if not status.get("ok"):
        raise HTTPException(
            status_code=409,
            detail=f"Username {username} does not exists",
        )
    return status
