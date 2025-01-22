from sqlalchemy import Column, VARCHAR, Uuid, ForeignKey

from database.config import Base
import uuid

class TeamModels(Base):
    __tablename__ = "teams"
    teamId = Column(Uuid, primary_key=True, default=uuid.uuid4)
    teamName = Column(VARCHAR)
    coachId = Column(ForeignKey("users.userId"))

    def __init__(self, teamName: str, coachId: Uuid):
        self.teamName = teamName
        self.coachId = coachId

    