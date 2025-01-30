from datetime import datetime

from sqlalchemy import select, delete, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import uuid

from models.event import EventModel
from models.user import UserModel
from models.enums import State
import schemas.team as team_schema
import schemas.user as user_schema
import schemas.event as event_schema
import models.junction_tables as junction_tables



class EventCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_event_by_eventname(self, eventName: str):
        stmt = select(EventModel).where(EventModel.eventName == eventName)
        result = await self.db_session.execute(stmt)
        team = result.scalars().first()
        return team
    
    async def get_events(self) -> List[event_schema.EventDB]:
        stmt = select(EventModel)
        result = await self.db_session.execute(stmt)
        events = result.scalars().all()
        return events
    
    async def get_event_by_id(self, eventId: str):
        stmt = select(EventModel).where(EventModel.eventId == eventId)
        result = await self.db_session.execute(stmt)
        event = result.scalars().first()
        return event
    
    async def create_event(self, event: event_schema.Event, teamId: uuid.UUID) -> event_schema.EventDB:
        db_event = EventModel(
            eventName=event.eventName,
            description=event.description,
            date=event.date,
            isSeries=event.isSeries,
            teamId=teamId
        )
        self.db_session.add(db_event)
        await self.db_session.commit()
        return db_event
    
    async def update_event(self, eventId: str, updated_event: event_schema.Event):
        stmt = (
            update(EventModel)
            .where(EventModel.eventId == eventId)
            .values(
                eventName=updated_event.eventName,
                description=updated_event.description,
                date=updated_event.date,
                isSeries=updated_event.isSeries
            )
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
    
    async def delete_event(self, eventId: str):
        stmt = delete(EventModel).where(EventModel.eventId == eventId)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)


    async def get_players_by_event(self, eventId: str) -> List[dict]:
        stmt = select(UserModel, junction_tables.events_users.c.state).join(
            junction_tables.events_users, UserModel.userId == junction_tables.events_users.c.user_id
        ).where(junction_tables.events_users.c.event_id == eventId)
        result = await self.db_session.execute(stmt)
        players = result.fetchall()
        return [{"userId": player.UserModel.userId, "eventId": eventId, "state": player.state} for player in players]
    

    async def add_player_to_event(self, eventId: str, playerId: str):
        stmt = insert(junction_tables.events_users).values(event_id=eventId, user_id=playerId)
        await self.db_session.execute(stmt)
        await self.db_session.commit()

    async def get_events_by_team(self, teamId: str):
        stmt = select(EventModel).where(EventModel.teamId == teamId)
        result = await self.db_session.execute(stmt)
        events = result.scalars().all()
        return events
    

    async def confirm_event(self, eventId: str, userId: str):
        stmt = (
            update(junction_tables.events_users)
            .where(junction_tables.events_users.c.event_id == eventId)
            .where(junction_tables.events_users.c.user_id == userId)
            .values(state=State.CONFIRMED)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
        await self.db_session.commit()


    async def decline_event(self, eventId: str, userId: str):
        stmt = (
            update(junction_tables.events_users)
            .where(junction_tables.events_users.c.event_id == eventId)
            .where(junction_tables.events_users.c.user_id == userId)
            .values(state=State.DECLINED)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
        await self.db_session.commit()