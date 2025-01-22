from sqlalchemy import Column, VARCHAR, Uuid, DateTime, Boolean, ForeignKey

from database.config import Base
import uuid

class EventModels(Base):
    __tablename__ = "events"
    eventId = Column(Uuid, primary_key=True, default=uuid.uuid4)
    eventName = Column(VARCHAR)
    description = Column(VARCHAR)
    date = Column(DateTime)
    isSeries = Column(Boolean)
    teamId = Column(ForeignKey("teams.teamId"))

    def __init__(self, eventName: str, description: str, date: DateTime, isSeries: Boolean, teamId: Uuid):
        self.eventName = eventName
        self.description = description
        self.date = date
        self.isSeries = isSeries
        self.teamId = teamId