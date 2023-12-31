from datetime import date, datetime

from pydantic import BaseModel


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        orm_mode = True


class SNewBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

    class Config:
        orm_mode = True


class OneMoreBooking(BaseModel):
    user_id: int
    room_id: int

    class Config:
        orm_mode = True
