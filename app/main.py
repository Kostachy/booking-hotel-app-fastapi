from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqladmin import Admin

from app.admin.auth import authentication_backend
from app.admin.views import BookingsAdmin, HotelsAdmin, RoomsAdmin, UsersAdmin
from app.bookings.router import router as booking_router
from app.config import settings
from app.database import engine
from app.hotels.rooms.router import router as rooms_router
from app.hotels.router import router as hotel_router
from app.images.router import router as image_router
from app.pages.router import router as page_router
from app.user.router import router as user_router

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


admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(UsersAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)
admin.add_view(BookingsAdmin)


@app.get("/")
async def root():
    return HTMLResponse('---SOON---')
