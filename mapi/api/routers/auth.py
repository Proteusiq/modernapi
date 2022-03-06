from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from mapi.schemas.token import Token
from mapi.core import security
from mapi.database.session import get_user_role

router = APIRouter(
    prefix="/token",
    tags=["authentication"],
)


@router.post("/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = security.authentificate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)

    role = get_user_role(username=form_data.username)
    access_token = security.create_access_token(
        data={"sub": user.username, "scopes": [*form_data.scopes, role]},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}
