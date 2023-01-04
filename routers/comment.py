from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.db_comment import get_all_comments_db, create_comment_db
from routers.schemas import CommentBase, UserAuth
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/comment',
    tags=['comment'],
)


@router.get('/all/{post_id}')
def create_comment(post_id: int, db: Session = Depends(get_db)):
    return get_all_comments_db(db, post_id)


@router.post('')
def create_comment(request: CommentBase, db: Session = Depends(get_db),
                   current_user: UserAuth = Depends(get_current_user)):
    return create_comment_db(db, request)
