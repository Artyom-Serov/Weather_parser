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


def save_weather_to_db(weater_data):
    session = Session()
    weather = models.Weather(
        temp=weater_data['temp'],
        pressure=weater_data['pressure'],
        wind_speed=weater_data['wind_speed'],
        wind_deg=weater_data['wind_deg'],
        rain=weater_data['rain'],
        snow=weater_data['snow']
    )
    session.add(weather)
    session.commit()
    session.close()
