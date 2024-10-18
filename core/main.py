"""Модуль для запуска проекта."""

import asyncio
import daemon
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


def run_as_daemon():
    """
    Функция для запуска основного процесса в режиме демона.
    """
    with daemon.DaemonContext():
        asyncio.run(main())


if __name__ == "__main__":
    """
    Точка входа для запуска скрипта в фоновом режиме.
    """
    run_as_daemon()

