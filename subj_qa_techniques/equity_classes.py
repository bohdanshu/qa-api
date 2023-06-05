import random

from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional


class ClientReference(BaseModel):
    age: int = Field(gt=17, description="Client age", title="Client's Age")


class BuildEquity(BaseModel):
    sequences: list = Field(description="sequences to build equity")

    class Config:
        schema_extra = {
            "example": {
                "sequences": ["1-10", "11-20", "33-100"]
                }
        }


router = APIRouter()


@router.post("/equity_classes", tags=["equity classes"], description="Route that gives response based on age passed; \nage ranges are 0-17, 18-30, 31-60, 61-...")
async def equity_classes(client_ref: ClientReference):
    if client_ref.age <= 17:
        return {"message": "No credits available for client younger than 18 years old"}
    elif 18 <= client_ref.age <= 30:
        return {"message": "There are some small credits available for youngsters"}
    elif 31 <= client_ref.age <= 60:
        return {"message": "There are lots of credits available for your age category, especially for business funding"}
    else:
        return {"message": "No credits available for client older than 60 years old"}


@router.post("/equity_classes/build", tags=["equity classes"])
async def build_equity(item: BuildEquity):
    seq = [[int(y) for y in x.split("-")] for x in item.sequences]
    resp = {}
    for sequence in seq:
        resp[f"value{seq.index(sequence)}"] = random.randint(sequence[0], sequence[1])
    return resp


@router.post("/buy_weapon", tags=["equity classes"], description="Route that gives age-based response on weapon buyer status; age ranges are 0-17, 18-20, 21-24, 25-...")
async def equity_classes(client_ref: ClientReference):
    if 18 <= client_ref.age < 21:
        return {"message": "Ви маєте право на придбання холодної, охолощеної та пневматичної зброї та основних частин до неї "}
    elif 21 <= client_ref.age < 25:
        return {"message": "Ви маєте право на придбання холодної, охолощеної та пневматичної зброї та основних частин до неї, а також  мисливську гладкоствольну зброю та основні частини до неї"}
    elif client_ref.age >= 25:
        return {"message": "Ви маєте право на придбання холодної, охолощеної, пневматичної, мисливської гладкоствольної, мисливської нарізної зброї та основних частин до неї"}
    else:
        return {"message": "Ви не можете придбати зброю"}


@router.get("/buy_weapon/build", tags=["equity classes"])
async def build_equity():
    resp = {"val1": random.randint(0, 20), "val2": random.randint(21, 24), "val3": random.randint(25, 100)}
    return resp

