from model import Creature
from fastapi import FastAPI, Depends, Query

app = FastAPI()


@app.get("/creature")
def get_all() -> list[Creature]:
    from data import get_creatures

    return get_creatures()


def user_dep(name: str = Query(...), password: str = Query(...)) -> dict:
    return {"name": name, "valid": True}


@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user
