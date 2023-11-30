from enum import Enum
from typing import Optional, List
from uuid import uuid4, UUID
from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    famale = "famale"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    surname: str
    gender: Gender
    role: List[Role]
