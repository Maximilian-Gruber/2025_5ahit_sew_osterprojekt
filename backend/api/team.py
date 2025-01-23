from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from auth.action import get_current_user
from crud.team import TeamCRUD
from crud.dependencies import get_team_crud
import schemas.team as team_schema
import schemas.user as user_schema
from models.enums import Role

router = APIRouter(prefix="/teams", tags=["teams"])

@router.post("")
async def register(
    new_team: team_schema.Team, db: TeamCRUD = Depends(get_team_crud), current_user: user_schema.UserDB = Depends(get_current_user)
):
    if current_user.role != Role.COACH:
        raise HTTPException(status_code=403, detail="Only coaches can create teams")
    db_team = await db.get_team_by_teamname(teamName=new_team.teamName)
    if db_team:
        raise HTTPException(status_code=409, detail="Team already registered")
    await db.create_team(team=new_team, user=current_user)
    return status.HTTP_201_CREATED


@router.get("")
async def get_teams(db: TeamCRUD = Depends(get_team_crud), current_user: user_schema.User = Depends(get_current_user)):
    return await db.get_teams() 


@router.get("/{teamId}")
async def get_team(teamId: str, db: TeamCRUD = Depends(get_team_crud), current_user: user_schema.User = Depends(get_current_user)):
    team = await db.get_team_by_id(teamId=teamId)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@router.delete("/{teamId}")
async def delete_team(teamId: str, db: TeamCRUD = Depends(get_team_crud), current_user: user_schema.UserDB = Depends(get_current_user)):
    team = await db.get_team_by_id(teamId=teamId)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    if current_user.role != Role.COACH:
        raise HTTPException(status_code=403, detail="Only coaches can delete teams")
    await db.delete_team(teamId=teamId)
    return status.HTTP_200_OK


@router.post("/{teamId}/players/{playerId}")
async def add_player_to_team(teamId: str, playerId: str, db: TeamCRUD = Depends(get_team_crud), current_user: user_schema.UserDB = Depends(get_current_user)):
    team = await db.get_team_by_id(teamId=teamId)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    if current_user.role != Role.COACH:
        raise HTTPException(status_code=403, detail="Only coaches can add players to teams")
    await db.add_player_to_team(teamId=teamId, playerId=playerId)
    return status.HTTP_200_OK


@router.get("/{teamId}/players")
async def get_players_per_team(teamId: str, db: TeamCRUD = Depends(get_team_crud), current_user: user_schema.User = Depends(get_current_user)):
    team = await db.get_team_by_id(teamId=teamId)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    players = await db.get_players_per_team(teamId=teamId)
    return players