from fastapi import FastAPI

from app.user.router import router as user_router
from app.bookings.router import router as booking_router


app = FastAPI(title='BookingAPI',
              description='API for booking hotels in your city')

app.include_router(user_router)
app.include_router(booking_router)
