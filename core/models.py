"""Модуль для работы с моделями."""

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Weather(Base):
    """
    Модель SQLAlchemy для хранения данных о погоде.

    Attributes:
        id (int): Уникальный идентификатор записи.
        temperature (int): Температура.
        pressure (int): Атмосферное давление (в мм рт. ст.).
        wind_speed (float): Скорость ветра.
        wind_deg (str): Направление ветра.
        rain (float): Количество осадков (дождь) за последний час.
        snow (float): Количество осадков (снег) за последний час.
    """
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Integer, nullable=False)
    pressure = Column(Integer, nullable=False)
    wind_speed = Column(Float, nullable=False)
    wind_deg = Column(String, nullable=False)
    rain = Column(Float, nullable=True)
    snow = Column(Float, nullable=True)
