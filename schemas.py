from pydantic import BaseModel
from datetime import date

class TransactionBase(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: str | None = None

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str
    role: str