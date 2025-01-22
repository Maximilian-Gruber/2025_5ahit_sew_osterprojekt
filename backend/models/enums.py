from enum import Enum

class Role(Enum):
    COACH = "coach"
    PLAYER = "player"

class State(Enum):
    CONFIRMED = "confirmed"
    DECLINED = "declined"
    PENDING = "pending"