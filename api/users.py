from typing import Optional, List

import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


users = []


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def post_user(user: User):
    users.append(user)
    return "Success"


@router.get("/users/active", response_model=List[User])
async def get_active_users():
    active_users = []
    for user in users:
        if user.is_active:
            active_users.append(user)
    return active_users


@router.get("/users/{id}")
async def get_user(id: int):
    return users[id]
