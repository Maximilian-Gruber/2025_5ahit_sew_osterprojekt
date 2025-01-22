import uuid
from pydantic import BaseModel
from models.enums import Role

# User Schema

class User(BaseModel):
    username: str
    password: str
    role: Role | None

class UserDB(User):
    userId: uuid.UUID
