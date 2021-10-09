from typing import Optional, Literal
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
    access_level: Optional[Literal[1, 3, 5]] = 1
