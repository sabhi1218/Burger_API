from pydantic import BaseModel
from typing import List

class StockCreate(BaseModel):
    item: str
    quantity: int


class StockResponse(BaseModel):
    item: str
    quantity: int

    class Config:
        orm_mode = True


class BurgerCountResponse(BaseModel):
    burgers: int


