from fastapi import APIRouter, HTTPException

from app.user.auth import get_password_hash
from app.user.dao import UsersDAO
from app.user.schema import SUserRegister

router = APIRouter(
    prefix='/auth',
    tags=['Авторизация пользователя']
)


@router.post('/register')
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=401)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add_new(email=user_data.email, hashed_password=hashed_password)
    return {'message': 'OK'}
