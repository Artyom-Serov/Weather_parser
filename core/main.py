"""Модуль для запуска проекта."""

import asyncio
from core.database import save_weather_to_db
from core.requests import get_weather


async def main():
    """
    Основная асинхронная функция для регулярного запроса данных о погоде и
    их сохранения в базу данных. Цикл выполняется каждые 3 минуты.
    """
    while True:
        weather_data = await get_weather()
        save_weather_to_db(weather_data)
        await asyncio.sleep(180)


if __name__ == "__main__":
    """
    Точка входа в программу. Запускает основную функцию main и 
    обрабатывает прерывание программы вручную.
    """
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Программа остановлена вручную")
