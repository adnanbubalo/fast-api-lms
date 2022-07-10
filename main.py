from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    license_info={
        "name": "FIT",
    },
)


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


users = []


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def post_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/active", response_model=List[User])
async def get_active_users():
    active_users = []
    for user in users:
        if user.is_active:
            active_users.append(user)
    return active_users


@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The id of the user you want to retrieve", lt=len(users)),
                   q: str = Query(None, max_length=5)
                   ):
    return {"user": users[id], "query": q}
