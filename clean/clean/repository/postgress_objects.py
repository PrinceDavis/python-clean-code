from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    code = Column(String(36), nullable=False)
    size = Column(Integer)
    price = Column(Integer)
    longtitude = Column(Float)
    latitude = Column(Float)
