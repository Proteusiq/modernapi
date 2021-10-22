from fastapi import APIRouter, Depends
from schemas.user import User
from core import security


router = APIRouter(prefix="/users", tags=["User"],)


@router.get("/me/", response_model=User)
async def read_users_me(current_user: User = Depends(security.get_current_active_user)):
    return current_user

