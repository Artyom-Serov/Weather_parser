"""Модуль для импорта данных из базы данных."""

import os
import sqlite3
import pandas as pd

# DB_PATH = '../weather.db'
# EXPORT_PATH = '../weather_data_export.xlsx'


def export_to_excel(
db_path='../weather.db', export_path='../weather_data_export.xlsx'
):
    """
    Экспортирует последние 10 записей из базы данных weather.db в файл
    формата .xlsx.

    Проверяет наличие базы данных, и если она отсутствует, выводит
    соответствующее сообщение. Загружает последние 10 записей из таблицы
    weather и сохраняет их в файл weather_data_export.xlsx.
    Если происходит ошибка при работе с базой данных, выводит
    сообщение об ошибке.
    """
    if not os.path.exists(db_path):
        print("Отсутствует искомая база данных для экспорта")
        return

    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(
            'SELECT * FROM weather ORDER BY id DESC LIMIT 10', conn
        )

        df.columns = ['ID', 'Температура, °C', 'Давление, мм рт. ст.',
                      'Скорость ветра, м/с', 'Направление ветра',
                      'Количество осадков (дождь), мм',
                      'Количество осадков (снег), мм']

        df.to_excel(export_path, index=False)
        print(f"Данные успешно экспортированы в {export_path}")

        conn.close()

    except Exception as error:
        print(f"Ошибка при работе с базой данных: {error}")


if __name__ == "__main__":
    export_to_excel()
