from typing import Generator

from database.config import async_session
from crud.user import UserCRUD
from crud.team import TeamCRUD


async def get_db() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield session


async def get_user_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield UserCRUD(session)

async def get_team_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield TeamCRUD(session)
