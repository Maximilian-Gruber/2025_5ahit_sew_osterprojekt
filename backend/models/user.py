from sqlalchemy import Column, String, Uuid, Enum

from database.config import Base
from models.enums import Role
import uuid

class UserModel(Base):
    __tablename__ = "users"
    userId = Column(Uuid, primary_key=True, default=uuid.uuid4)
    username = Column(String)
    password = Column(String)
    role = Column(Enum(Role), default=Role.PLAYER)

    def __init__(self, username: str, password: str, role: Role) -> None:
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self) -> str:
        return f"<UserModels(username={self.username}, password={self.password})>"
