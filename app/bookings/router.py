from fastapi import APIRouter
from app.bookings.schema import SBooking
from app.bookings.dao import BookingDAO
from typing import List

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get('', response_model=List[SBooking])
async def get_bookings():
    return await BookingDAO.find_all()


@router.get('/{id}')
async def get_id(id: int):
    return await BookingDAO.get_by_id(id)
