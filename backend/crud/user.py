from datetime import datetime

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from auth.utils import get_password_hash
from models.user import UserModel
import schemas.user as user_schema


class UserCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_user_by_username(self, username: str):
        stmt = select(UserModel).where(UserModel.username == username)
        result = await self.db_session.execute(stmt)
        user = result.scalars().first()
        return user

    async def get_users(self) -> List[user_schema.UserDB]:
        stmt = select(UserModel)
        result = await self.db_session.execute(stmt)
        users = result.scalars().all()
        return users

    async def create_user(self, user: user_schema.User) -> user_schema.UserDB:
        db_user = UserModel(
            username=user.username,
            password=get_password_hash(user.password),
            role=user.role
        )
        self.db_session.add(db_user)
        await self.db_session.commit()
        return db_user

    async def delete_user(self, username: str):
        stmt = delete(UserModel).where(UserModel.username == username)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
