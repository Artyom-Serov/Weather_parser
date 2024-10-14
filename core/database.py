"""Модуль для работы с базой данных."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import models

Base = declarative_base()

DATABASE_URL = "sqlite:///weather.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def save_weather_to_db(weather_data):
    session = Session()
    weather = models.Weather(
        temp=weather_data['temp'],
        pressure=weather_data['pressure'],
        wind_speed=weather_data['wind_speed'],
        wind_deg=weather_data['wind_deg'],
        rain=weather_data['rain'],
        snow=weather_data['snow']
    )
    session.add(weather)
    session.commit()
    session.close()
