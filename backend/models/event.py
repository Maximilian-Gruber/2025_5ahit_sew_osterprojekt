from sqlalchemy import Column, Uuid, DateTime, Boolean, ForeignKey, String

from database.config import Base
import uuid

class EventModel(Base):
    __tablename__ = "events"
    eventId = Column(Uuid, primary_key=True, default=uuid.uuid4)
    eventName = Column(String)
    description = Column(String)
    date = Column(DateTime(timezone=True))
    isSeries = Column(Boolean)
    teamId = Column(ForeignKey("teams.teamId", ondelete="CASCADE"))

    def __init__(self, eventName: str, description: str, date: DateTime, isSeries: Boolean, teamId: Uuid):
        self.eventName = eventName
        self.description = description
        self.date = date
        self.isSeries = isSeries
        self.teamId = teamId