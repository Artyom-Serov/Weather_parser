"""Модуль для работы с запросами от внешних ресурсов."""
from typing import Dict, Any

import aiohttp
import asyncio
import sqlalchemy

API_KEY = "99ba78ee79a2a24bc507362c5288a81b"
API_URL = "https://api.openweathermap.org/data/2.5/weather?lat=55.42&lon=37.22&appid={}&units=metric".format(API_KEY)


async def get_weather():
    try:
        async with aiohttp.ClientSession as session:
            async with session.get(API_URL) as response:
                data = await response.json()
                main = data['main']
                wind = data['wind']
                rain = data.get('rain', {}).get('1h', None)
                snow = data.get('snow', {}).get('1h', None)
                weather_data: dict[str, Any] = {
                    "temp": main['temp'],
                    "pressure": main['pressure'],
                    "wind_speed": wind['speed'],
                    "wind_deg": wind['deg'],
                    "rain": rain,
                    "snow": snow
                }
                return weather_data
    except aiohttp.ClientError as error:
        print(f"Ошибка соединения: {error}")
