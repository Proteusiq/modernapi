from typing import Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    username: Optional[str] = Field(default=None, primary_key=True)
    email: str
    full_name: str
    disabled: Optional[bool] = None


class UserInDB(SQLModel, table=True):
    username: Optional[str] = Field(default=None, primary_key=True)
    email: str
    full_name: str
    disabled: Optional[bool] = None
    hashed_password: str
