"""Модуль для запуска проекта."""

import asyncio
import daemon
import os
from core.database import save_weather_to_db
from core.requests import get_weather
import logging
import sys

logging.basicConfig(
    filename='weather_daemon.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)


def run():
    """
    Основная функция для запуска цикла асинхронных запросов в фоновом режиме.
    Выполняет запросы каждые 3 минуты и сохраняет данные в базу.
    """

    async def main():
        while True:
            weather_data = await get_weather()
            if weather_data is None:
                logging.error('Не удалось получить данные о погоде.')
            else:
                save_weather_to_db(weather_data)
                logging.info(
                    'Данные о погоде успешно сохранены в базу данных.'
                )
            await asyncio.sleep(180)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)


def start_daemon():
    """
    Функция для запуска процесса в режиме демона.
    """
    with daemon.DaemonContext(
            working_directory=os.getcwd(),
            stdout=open('weather_daemon_out.log', 'a+', buffering=1),
            stderr=open('weather_daemon_err.log', 'a+', buffering=1),
            umask=0o002
    ):
        run()


if __name__ == "__main__":
    """
    Точка входа в программу. Запускает функцию start_daemon для работы в фоновом режиме.
    """
    try:
        start_daemon()
    except Exception as error:
        logging.error(f"Ошибка при запуске демона: {error}")
        sys.exit(1)

