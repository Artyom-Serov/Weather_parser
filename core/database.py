"""Модуль для работы с базой данных."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.models import Base, Weather

DATABASE_URL = "sqlite:///../weather.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def convert_wind_deg_to_direction(deg):
    if deg >= 0 and deg < 45 or deg == 360:
        return "С"
    elif deg >= 45 and deg < 90:
        return "СВ"
    elif deg >= 90 and deg < 135:
        return "В"
    elif deg >= 135 and deg < 180:
        return "ЮВ"
    elif deg >= 180 and deg < 225:
        return "Ю"
    elif deg >= 225 and deg < 270:
        return "ЮЗ"
    elif deg >= 270 and deg < 315:
        return "З"
    elif deg >= 315 and deg < 360:
        return "СЗ"


def save_weather_to_db(weather_data):
    if weather_data is None:
        print("Нет данных для сохранения в базу")
    session = Session()
    updated_temperature = round(weather_data['temp'])
    updated_pressure = round(weather_data['pressure'] * 0.75)
    wind_direction = convert_wind_deg_to_direction(weather_data['wind_deg'])
    weather = Weather(
        temp=updated_temperature,
        pressure=updated_pressure,
        wind_speed=weather_data['wind_speed'],
        wind_deg=wind_direction,
        rain=weather_data['rain'],
        snow=weather_data['snow']
    )
    session.add(weather)
    session.commit()
    session.close()
