from datetime import date

from fastapi import APIRouter, Depends
# from app.bookings.schema import SBooking
from app.bookings.dao import BookingDAO

from app.user.dependencies import get_current_user
from app.user.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):
    return user


@router.post('')
async def add_bookings(room_id: int,
                       date_from: date,
                       date_to: date,
                       user: Users = Depends(get_current_user)
                       ):
    await BookingDAO.add(user.id, room_id, date_from, date_to)
    return {'message': 'OK'}


@router.get('/{us_id}')
async def get_id(us_id: int):
    return await BookingDAO.get_by_id(us_id)
