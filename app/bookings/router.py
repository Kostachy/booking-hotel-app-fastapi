from fastapi import APIRouter, Depends
from app.bookings.schema import SBooking
from app.bookings.dao import BookingDAO
from typing import List

from app.user.dependencies import get_current_user
from app.user.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):
    print(user, type(user), user.email)
    return user


@router.get('/{id}')
async def get_id(id: int):
    return await BookingDAO.get_by_id(id)
