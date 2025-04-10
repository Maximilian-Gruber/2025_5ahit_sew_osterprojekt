from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from auth.action import get_current_user
from crud.event import EventCRUD
from crud.team import TeamCRUD
from crud.dependencies import get_event_crud
from crud.dependencies import get_team_crud
import schemas.team as team_schema
import schemas.user as user_schema
import schemas.event as event_schema
from models.enums import Role

router = APIRouter(prefix="/events", tags=["events"])

@router.post("")
async def create_event(
    new_event: event_schema.Event, db: EventCRUD = Depends(get_event_crud), current_user: user_schema.UserDB = Depends(get_current_user)
):
    if current_user.role != Role.COACH:
        raise HTTPException(status_code=403, detail="Only coaches can create events")
    await db.create_event(event=new_event, teamId=new_event.teamId)
    return status.HTTP_201_CREATED  


@router.get("")
async def get_events(db: EventCRUD = Depends(get_event_crud), current_user: user_schema.User = Depends(get_current_user)):
    return await db.get_events()


@router.get("/{eventId}")
async def get_event(eventId: str, db: EventCRUD = Depends(get_event_crud), current_user: user_schema.User = Depends(get_current_user)):
    event = await db.get_event_by_id(eventId=eventId)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{eventId}")
async def update_event(eventId: str, updated_event: event_schema.Event, db: EventCRUD = Depends(get_event_crud), current_user: user_schema.UserDB = Depends(get_current_user)):
    event = await db.get_event_by_id(eventId=eventId)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if current_user.role != Role.COACH:
        raise HTTPException(status_code=403, detail="Only coaches can update events")
    await db.update_event(eventId=eventId, updated_event=updated_event)
    return status.HTTP_200_OK


@router.delete("/{eventId}")
async def delete_event(eventId: str, db: EventCRUD = Depends(get_event_crud), current_user: user_schema.UserDB = Depends(get_current_user)):
    event = await db.get_event_by_id(eventId=eventId)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if current_user.role != Role.COACH:
        raise HTTPException(status_code=403, detail="Only coaches can delete events")
    await db.delete_event(eventId=eventId)
    return status.HTTP_200_OK


@router.get("/{eventId}/players")
async def get_players_by_event(eventId: str, db: EventCRUD = Depends(get_event_crud), current_user: user_schema.User = Depends(get_current_user)):
    event = await db.get_event_by_id(eventId=eventId)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return await db.get_players_by_event(eventId=eventId)


@router.post("/{eventId}/players/{playerId}")
async def add_player_to_event(eventId: str, playerId: str, db: EventCRUD = Depends(get_event_crud), current_user: user_schema.UserDB = Depends(get_current_user)):
    event = await db.get_event_by_id(eventId=eventId)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if current_user.role != Role.COACH:
        raise HTTPException(status_code=403, detail="Only coaches can add players to events")
    await db.add_player_to_event(eventId=eventId, playerId=playerId)
    return status.HTTP_200_OK


@router.get("/{teamId}")
async def get_events_by_team(teamId: str, db_event: EventCRUD = Depends(get_event_crud), db_team: TeamCRUD = Depends(get_team_crud), current_user: user_schema.User = Depends(get_current_user)):
    team = await db_team.get_team_by_id(teamId=teamId)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return await db_event.get_events_by_team(teamId=teamId)


@router.post("/confirm/")
async def confirm_event(eventId: str, db: EventCRUD = Depends(get_event_crud), current_user: user_schema.UserDB = Depends(get_current_user)):
    if current_user.role != Role.COACH:
        raise HTTPException(status_code=403, detail="Only coaches can confirm events")
    await db.confirm_event(eventId=eventId, userId=current_user.userId)
    return status.HTTP_200_OK


@router.post("/decline/")
async def decline_event(eventId: str, db: EventCRUD = Depends(get_event_crud), current_user: user_schema.UserDB = Depends(get_current_user)):
    if current_user.role != Role.COACH:
        raise HTTPException(status_code=403, detail="Only coaches can decline events")
    await db.decline_event(eventId=eventId, userId=current_user.userId)
    return status.HTTP_200_OK