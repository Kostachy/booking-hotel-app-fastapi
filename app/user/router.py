from fastapi import APIRouter, Depends, Response

from app.exception import IncorrectEmailOrPasswordException, UserAlreadyExistsException
from app.user.auth import authenticate_user, create_access_token, get_password_hash
from app.user.dao import UsersDAO
from app.user.dependencies import get_current_user
from app.user.models import Users
from app.user.schema import SUserAuth

router = APIRouter(
    prefix='/auth',
    tags=['Авторизация пользователя']
)


@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add_new(email=user_data.email, hashed_password=hashed_password)
    return {'message': 'OK'}


@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('booking_access_token', access_token, httponly=True)
    return {'token': access_token}


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('booking_access_token')
    return {'message': 'success logout'}


@router.get('/me')
async def read_user_me(current_user: Users = Depends(get_current_user)):
    return current_user
