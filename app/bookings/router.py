from datetime import date

from fastapi import APIRouter, Depends
from pydantic import parse_obj_as

from app.bookings.dao import BookingDAO
from app.bookings.schema import SNewBooking
from app.exception import RoomCannotBeBooked
from app.tasks.app_tasks import send_booking_confirm_email
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
async def add_bookings(
        room_id: int,
        date_from: date,
        date_to: date,
        user: Users = Depends(get_current_user)
):
    bookings = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not bookings:
        raise RoomCannotBeBooked
    bookings = parse_obj_as(SNewBooking, bookings).dict()
    send_booking_confirm_email.delay(bookings, user.email)
    return bookings


@router.get('/{us_id}')
async def get_id(us_id: int):
    return await BookingDAO.get_by_id(us_id)


@router.delete("/{booking_id}")
async def remove_booking(booking_id: int, current_user: Users = Depends(get_current_user)):
    await BookingDAO.delete(id=booking_id, user_id=current_user.id)
