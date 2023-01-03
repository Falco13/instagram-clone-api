from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from routers.schemas import PostBase, PostDisplay, UserAuth
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.db_post import create_post_db, get_all_posts_db
from auth.oauth2 import get_current_user
from typing import List
import random
import string
import shutil

router = APIRouter(prefix='/post',
                   tags=['post'],
                   )

image_url_type = ['absolute', 'relative']


@router.post('', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_type:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Parameter image_url_type can only take values 'absolute' or 'relative'.")
    return create_post_db(db, request)


@router.get('/all', response_model=List[PostDisplay])
def all_posts(db: Session = Depends(get_db)):
    return get_all_posts_db(db)


@router.post('/image')
def upload_image(image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(11))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}
