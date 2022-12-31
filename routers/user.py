from fastapi import APIRouter, Depends
from routers.schemas import UserDisplay, UserBase
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.db_user import create_user_db, get_all_users_db
from typing import List

router = APIRouter(prefix='/user',
                   tags=['user'],
                   )


@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return create_user_db(db, request)


@router.get('/all', response_model=List[UserDisplay])
def all_users(db: Session = Depends(get_db)):
    return get_all_users_db(db)
