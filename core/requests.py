"""Модуль для работы с запросами от внешних ресурсов."""

import aiohttp
import asyncio

API_KEY = "f812d2778ff654f9e460892c31bd1678"
API_URL = "https://api.openweathermap.org/data/2.5/weather?lat=55.42&lon=37.22&appid={}&units=metric".format(API_KEY)


async def get_weather():
    """
    Асинхронно выполняет GET-запрос к OpenWeather API для получения данных
    о погоде.

    Returns:
        dict: Словарь с данными о температуре, давлении, скорости и
        направлении ветра, а также осадках.
        None: Если произошла ошибка при выполнении запроса.
    """
    timeout = aiohttp.ClientTimeout(total=10)
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(API_URL) as response:
                data = await response.json()
                main = data['main']
                wind = data['wind']
                rain = data.get('rain', {}).get('1h', None)
                snow = data.get('snow', {}).get('1h', None)

                weather_data = {
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
    except asyncio.TimeoutError:
        print("Превышено время ожидания ответа от сервера")
    return None
