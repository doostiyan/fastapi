from fastapi import APIRouter, Depends
from database import db_user
from database.db import get_db
from schemas import UserDisplay, UserBase

router = APIRouter(prefix='/user', tags=['user'])

@router.post('/', response_model=UserDisplay)
def create_user(user: UserBase, db=Depends(get_db)):
    return db_user.create_user(db, user)