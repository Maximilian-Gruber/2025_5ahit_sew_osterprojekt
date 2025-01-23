import uuid
from pydantic import BaseModel
from models.enums import Role

# Team Schema

class Team(BaseModel):
    teamName: str
    coachId: uuid.UUID

class TeamDB(Team):
    teamId: uuid.UUID