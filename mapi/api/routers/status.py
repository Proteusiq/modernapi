from fastapi import APIRouter, Depends
from schemas.user import User
from core import security

router = APIRouter(prefix="/status", tags=["Health"],)


@router.get("/")
async def read_system_status(current_user: User = Depends(security.get_current_user)):
    current_user.disabled = False
    print(current_user.username)
    return {"status": "ok"}
