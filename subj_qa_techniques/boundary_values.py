from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class Investment(BaseModel):
    summ: int = Field(gt=0, lt=5000001)

    class Config:
        schema_details = {
            "example": {
                "summ": 250000
            }
        }


@router.post("/boundary/example1", tags=["boundary values"],
             description="""
                Функція що надає значення для тестування границь 
                Границі:
                1-1000: 0,5%
                1001-10000: 1%
                10001-100000: 1,5%
                100001-500000: 3%
                500001 - 5000000: індивідуальні пропозиції """
             )
async def main(item: Investment):
    if 0 > item.summ:
        return ValueError()
    if 1 <= item.summ <= 1000:
        return {"msg": "success", "offer": 0.5}
    elif 1000 < item.summ <= 10000:
        return {"msg": "success", "offer": 1.0}
    elif 10000 < item.summ <= 100000:
        return {"msg": "success", "offer": 1.5}
    elif 100000 < item.summ <= 500000:
        return {"msg": "success", "offer": 3.0}
    elif 500000 < item.summ <= 5000000:
        return {"msg": "success",
                "offer": "Будь ласка верніться до найближчого відділення для отримання персональної пропозиції "}
    else:
        return {"msg": "can't handle value"}


@router.get("/boundary/example1/build", tags=["boundary values"],
            description="""
                Функція що надає значення для тестування границь 
                Границі:
                1-1000: 0,5%
                1001-10000: 1%
                10001-100000: 1,5%
                100001-500000: 3%
                500001 - 5000000: індивідуальні пропозиції """
            )
async def main():
    resp = {
        "bound1": [[0, 1], [1000, 1001]],
        "bound2": [[1000, 1001], [10000, 10001]],
        "bound3": [[10000, 10001], [100000, 100001]],
        "bound4": [[100000, 100001], [500000, 500001]],
        "bound5": [[500000, 500001], [5000000, 5000001]],

    }
