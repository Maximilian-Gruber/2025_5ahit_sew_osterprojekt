import uuid
from pydantic import BaseModel

# Team Schema

class Team(BaseModel):
    teamName: str
    coachId: uuid.UUID

class TeamDB(Team):
    teamId: uuid.UUID


class TeamCreate(BaseModel):
    teamName: str