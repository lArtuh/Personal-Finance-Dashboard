from pydantic import BaseModel
from datetime import date


class CategoryBase(BaseModel):
    name: str
    type: str  # "income" or "expense"


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class TransactionBase(BaseModel):
    amount: float
    date: date
    description: str
    category_id: int


class TransactionCreate(TransactionBase):
    pass


class TransactionResponse(TransactionBase):
    id: int
    category: CategoryResponse

    class Config:
        orm_mode = True
