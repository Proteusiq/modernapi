from fastapi import APIRouter, Security, Depends
from schemas.user import User
from api import security

router = APIRouter(
    prefix="/users",
    tags=["User"],
)


@router.get("/me/", response_model=User)
async def read_users_me(current_user: User = Depends(security.get_current_active_user)):
    return current_user


@router.get("/me/items/")
async def read_own_items(
    current_user: User = Security(security.get_current_active_user, scopes=["items"])
):
    return [{"item_id": "Foo", "owner": current_user.username}]
