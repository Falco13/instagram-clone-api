from routers.schemas import UserBase
from db.models import DbUser
from sqlalchemy.orm.session import Session
from db.hashing import Hash


def create_user_db(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.get_password_hash(password=request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users_db(db: Session):
    return db.query(DbUser).all()
