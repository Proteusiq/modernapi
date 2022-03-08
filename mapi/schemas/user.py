# -*- coding: utf-8 -*-
from typing import Literal, Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = False
    role_name: Literal["admin", "visitor"] = "visitor"


class UserCreate(User):
    password: str


class UserUpdate(User):
    password: Optional[str] = None


class UserInDB(User):
    hashed_password: str
