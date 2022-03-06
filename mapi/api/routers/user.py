from fastapi import APIRouter, Depends
from mapi.schemas.user import User
from mapi.core import security


router = APIRouter(
    prefix="/users",
    tags=["user"],
)


@router.get("/me/", response_model=User)
async def read_users_me(current_user: User = Depends(security.get_current_active_user)):
    return current_user
