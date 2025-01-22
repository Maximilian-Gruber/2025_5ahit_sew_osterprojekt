from sqlalchemy import Table, Column, Integer, ForeignKey, Enum
from models.enums import State
from database.config import Base

user_teams = Table('user_teams', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('team_id', Integer, ForeignKey('teams.id'), primary_key=True)
)

events_users = Table('events_users', Base.metadata,
    Column('event_id', Integer, ForeignKey('events.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('state', Enum(State))
)