"""Модуль для моделей."""

from sqlalchemy import create_engine, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DATABASE_URL = "sqlite:///weather.db"


class Weather(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    temp = Column(Float, nullable=False)
    pressure = Column(Integer, nullable=False)
    wind_speed = Column(Float, nullbase=False)
    wind_deg = Column(Integer, nullbase=False)
    rain = Column(Float, nullbase=False)
    snow = Column(Float, nullbase=False)


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

