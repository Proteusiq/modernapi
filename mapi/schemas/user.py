from typing import Literal, Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    role_name: Literal["admin", "visitor"] = None


class UserCreate(User):
    password: str


class UserInDB(User):
    hashed_password: str
