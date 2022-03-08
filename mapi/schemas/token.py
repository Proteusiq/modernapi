# -*- coding: utf-8 -*-
from typing import Optional, Iterable
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: Iterable[str] = []
