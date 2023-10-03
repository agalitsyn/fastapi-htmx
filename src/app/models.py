from enum import Enum

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql import expression
from sqlalchemy_utils.types.choice import ChoiceType

from app.db import Base


class UserRoleEnum(str, Enum):
    admin = "admin"
    editor = "editor"
    regular = "regular"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(ChoiceType(UserRoleEnum), default=UserRoleEnum.regular, nullable=False)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=False, server_default=expression.false())
