"""Модуль для работы с моделями."""

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True, autoincrement=True)
    temp = Column(Float, nullable=False)
    pressure = Column(Integer, nullable=False)
    wind_speed = Column(Float, nullbase=False)
    wind_deg = Column(Integer, nullbase=False)
    rain = Column(Float, nullbase=False)
    snow = Column(Float, nullbase=False)
