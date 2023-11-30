from http import HTTPStatus
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        name="Necdet",
        surname="UYGUR",
        gender=Gender.male,
        role=[Role.admin],
    ),
    User(
        id=uuid4(),
        name="Meftun",
        surname="UYGUR",
        gender=Gender.male,
        role=[Role.user, Role.student],
    ),
]


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/users")
async def users():
    return db


@app.post("/users")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for item in db:
        if item.id == user_id:
            db.remove(item)
            return {"response": "OK"}
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail=f"User ID {user_id} not found!"
    )


@app.put("/users/{user_id}")
async def update_user(user_id: UUID, user: User):
    for item in db:
        if item.id == user_id:
            if user.name is not None:
                item.name = user.name
            if user.surname is not None:
                item.surname = user.surname
            if user.gender is not None:
                item.gender = user.gender
            if user.role is not None:
                item.role = user.role
            return {"response": "OK"}
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail=f"User ID {user_id} not found!"
    )
