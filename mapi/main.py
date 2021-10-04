from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from api import security
from models.users import User, UserInDB
from models.token import Token, TokenData
from core import auth
from core import user


app = FastAPI(
    title="Awesome API",
    description="Inspire By Prayson's Madness",
    version="0.0.1",
)


app.include_router(auth.router)
app.include_router(user.router)
