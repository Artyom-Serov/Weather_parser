"""Модуль для запуска проекта в фоновом режиме (в режиме демона)."""

import asyncio
from core.database import save_weather_to_db
from core.requests import get_weather
import daemon
import signal
import sys

async def main():
    """
    Основная асинхронная функция для регулярного запроса данных о погоде и
    их сохранения в базу данных. Цикл выполняется каждые 3 минуты.
    """
    def handle_signals():
        print("Демон завершает работу...")
        sys.exit(0)

    signal.signal(signal.SIGTERM, lambda sig, frame: handle_signals())

    while True:
        weather_data = await get_weather()
        save_weather_to_db(weather_data)
        await asyncio.sleep(180)

if __name__ == "__main__":
    """
    Точка входа в программу. Запускает основную функцию main в режиме демона.
    """
    daemon_context = daemon.DaemonContext(
        stdout=sys.stdout,
        stderr=sys.stderr,
        signal_map={
            signal.SIGTERM: signal.SIG_DFL,
        }
    )

    with daemon_context:
        asyncio.run(main())