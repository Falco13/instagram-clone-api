from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    id: str
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


class CommentPostDisplay(BaseModel):
    text: str
    username: str
    timestamp: datetime

    class Config:
        orm_mode = True


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    description: str
    timestamp: datetime
    user: UserForPostDisplay
    comments: List[CommentPostDisplay]

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str


class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int
