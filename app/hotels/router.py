from typing import Optional

from fastapi import APIRouter

from app.hotels.dao import HotelDAO
from app.hotels.schema import SHotel

router = APIRouter(prefix="/hotels", tags=["Отели"])


@router.get("/id/{hotel_id}", include_in_schema=True)
async def get_hotel_by_id(hotel_id: int,) -> Optional[SHotel]:
    return await HotelDAO.find_one_or_none(id=hotel_id)
