from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from auth.action import get_current_user
from crud.user import UserCRUD
from crud.dependencies import get_user_crud
import schemas.user as user_schema

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=List[user_schema.UserDB])
async def get_users(db: UserCRUD = Depends(get_user_crud), current_user: user_schema.User = Depends(get_current_user)):
    return await db.get_users()


@router.post("")
async def register(
    new_user: user_schema.User, db: UserCRUD = Depends(get_user_crud)
):
    db_user = await db.get_user_by_username(username=new_user.username)
    if db_user:
        raise HTTPException(status_code=409, detail="Username already registered")
    await db.create_user(new_user)
    return status.HTTP_201_CREATED


@router.delete("")
async def delete_user(
    current_user: user_schema.User = Depends(get_current_user),
    db: UserCRUD = Depends(get_user_crud),
):
    return await db.delete_user(username=current_user.username)
