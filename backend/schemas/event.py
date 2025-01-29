import uuid
from pydantic import BaseModel
from datetime import datetime

# Event Schema

class Event(BaseModel):
    eventName: str
    description: str
    date: datetime
    isSeries: bool
    teamId: uuid.UUID


class EventDB(Event):
    eventId: uuid.UUID