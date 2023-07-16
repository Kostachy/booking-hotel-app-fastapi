from fastapi import FastAPI

from app.user.router import router as user_router
from app.bookings.router import router as booking_router
from app.pages.router import router as page_router
from app.hotels.router import router as hotel_router
from app.hotels.rooms.router import router as rooms_router

app = FastAPI(title='BookingAPI',
              description='API for booking hotels in your city')

app.include_router(hotel_router)
app.include_router(rooms_router)
app.include_router(user_router)
app.include_router(booking_router)
app.include_router(page_router)
