from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin, ModelView

from app.admin.views import UserAdmin, BookingsAdmin
from app.config import settings
from app.database import engine
from app.user.models import Users
from app.user.router import router as user_router
from app.bookings.router import router as booking_router
from app.pages.router import router as page_router
from app.hotels.router import router as hotel_router
from app.hotels.rooms.router import router as rooms_router
from app.images.router import router as image_router

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

app = FastAPI(title='BookingAPI', description='API for booking hotels in your city')

app.mount('/static', StaticFiles(directory='app/static'), 'static')

app.include_router(hotel_router)
app.include_router(rooms_router)
app.include_router(user_router)
app.include_router(booking_router)
app.include_router(page_router)
app.include_router(image_router)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin",
                   "Authorization"],
)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(settings.REDIS_URL)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(BookingsAdmin)
