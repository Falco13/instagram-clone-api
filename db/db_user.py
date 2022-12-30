from routers.schemas import UserBase
from db.models import DbUser
from sqlalchemy.orm.session import Session


def create_user_db(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=request.password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
