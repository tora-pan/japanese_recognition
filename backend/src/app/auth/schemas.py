from datetime import date
from typing import Optional
from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[date] = None

    class Config:
      from_attributes = True