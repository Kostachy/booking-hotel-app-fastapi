from fastapi import FastAPI

from app.bookings.router import router as booking_router

app = FastAPI(title='BookingAPI',
              description='API for booking hotels in your city')

app.include_router(booking_router)
