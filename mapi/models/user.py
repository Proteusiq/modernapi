from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship



class Role(SQLModel, table=True):
    name: Optional[str] = Field(default="visitor", primary_key=True)
    users: List["UserInDB"] = Relationship(back_populates="role")



class User(SQLModel, table=True):
    username: str = Field(primary_key=True)
    email: str
    full_name: str
    disabled: Optional[bool] = None
    role_name: str = Field(default=None, foreign_key="role.name")


class UserInDB(SQLModel, table=True):
    username: Optional[str] = Field(default=None, primary_key=True)
    email: str
    full_name: str
    disabled: Optional[bool] = None
    hashed_password: str
    role_name : str = Field(default=None, foreign_key="role.name")
    role: Role = Relationship(back_populates="users")
    

