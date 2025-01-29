from sqlalchemy import Table, Column, Integer, ForeignKey, Enum, UUID
from models.enums import State
from database.config import Base

user_teams = Table('user_teams', Base.metadata,
    Column('user_id', UUID, ForeignKey('users.userId'), primary_key=True),
    Column('team_id', UUID, ForeignKey('teams.teamId'), primary_key=True)
)

events_users = Table('events_users', Base.metadata,
    Column('event_id', UUID, ForeignKey('events.eventId'), primary_key=True),
    Column('user_id', UUID, ForeignKey('users.userId'), primary_key=True),
    Column('state', Enum(State))
)