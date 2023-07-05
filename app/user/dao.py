from app.dao.base import BaseDAO
from app.user.models import Users


class UsersDAO(BaseDAO):
    model = Users
