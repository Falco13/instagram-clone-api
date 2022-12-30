from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from routers.schemas import PostBase, PostDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.db_post import create_post_db

router = APIRouter(prefix='/post',
                   tags=['post'],
                   )

image_url_type = ['absolute', 'relative']


@router.post('', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_type:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Parameter image_url_type can only take values 'absolute' or 'relative'.")
    return create_post_db(db, request)
