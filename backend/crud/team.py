from datetime import datetime

from sqlalchemy import select, delete, insert
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from models.team import TeamModel
import schemas.team as team_schema
import schemas.user as user_schema
import models.junction_tables as junction_tables


class TeamCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_team_by_teamname(self, teamName: str):
        stmt = select(TeamModel).where(TeamModel.teamName == teamName)
        result = await self.db_session.execute(stmt)
        team = result.scalars().first()
        return team
    
    async def get_teams(self) -> List[team_schema.TeamDB]:
        stmt = select(TeamModel)
        result = await self.db_session.execute(stmt)
        teams = result.scalars().all()
        return teams
    
    async def get_team_by_id(self, teamId: str):
        stmt = select(TeamModel).where(TeamModel.teamId == teamId)
        result = await self.db_session.execute(stmt)
        team = result.scalars().first()
        return team
    
    async def create_team(self, team: team_schema.Team, user: user_schema.UserDB) -> team_schema.TeamDB:
        db_team = TeamModel(
            teamName=team.teamName,
            coachId=user.userId
        )
        self.db_session.add(db_team)
        await self.db_session.commit()
        return db_team
    
    async def delete_team(self, teamId: str):
        stmt = delete(TeamModel).where(TeamModel.teamId == teamId)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def get_players_per_team(self, teamId: str):
        stmt = select(junction_tables.user_teams).where(junction_tables.user_teams.c.team_id == teamId)
        result = await self.db_session.execute(stmt)
        players = result.scalars().all()
        return players
    
    async def add_player_to_team(self, teamId: str, playerId: str):
        stmt = insert(junction_tables.user_teams).values(team_id=teamId, user_id=playerId)
        await self.db_session.execute(stmt)
        await self.db_session.commit()
