from sqlalchemy import Column, Integer, Date, ForeignKey, Computed
from app.database import Base


class Bookings(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed('(date_from - date_to) * price'))
    total_days = Column(Integer, Computed('date_from - date_to'))