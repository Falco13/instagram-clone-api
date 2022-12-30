from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


# for Posts

class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    description: str
    author_id: int


class UserForPostDisplay(BaseModel):
    username: str

    class Config:
        orm_mode = True


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    description: str
    timestamp: datetime
    user: UserForPostDisplay

    class Config:
        orm_mode = True
