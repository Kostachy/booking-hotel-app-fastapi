from sqlalchemy import select
from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def get_all(cls, **filter_arg):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by()
            result = await session.execute(query)
            return result.mappings().all()
