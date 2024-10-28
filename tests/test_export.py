import os
import unittest
from sqlite3 import connect

import pandas as pd
import sqlite3
from core.export import export_to_excel

TEST_DB_PATH = '../test_weather.db'
TEST_EXPORT_PATH = '../test_weather_export.xlsx'


def create_test_bd():
    conn = sqlite3.connect(TEST_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature INTEGER,
            pressure INTEGER,
            wind_speed REAL,
            wind_deg TEXT,
            rain REAL,
            snow REAL
        )
    ''')

    for i in range(13):
        cursor.execute('''
            INSERT INTO weather (temperature, pressure, wind_speed, wind_deg, rain, snow)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (20 + i, 760, 5.5, 'З', 0.0, 0.0))

    conn.commit()
    conn.close()


def cleanup_test_files():
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    if os.path.exists(TEST_EXPORT_PATH):
        os.remove(TEST_EXPORT_PATH)


class TestExport(unittest.TestCase):
    def setUp(self):
        create_test_bd()

    def tearDown(self):
        cleanup_test_files()

    def test_export_to_excel(self):
        export_to_excel(db_path=TEST_DB_PATH, export_path=TEST_EXPORT_PATH)
        self.assertTrue(os.path.exists(TEST_EXPORT_PATH))

        df = pd.read_excel(TEST_EXPORT_PATH)
        self.assertEqual(len(df), 10)

        conn = sqlite3.connect(TEST_DB_PATH)
        df_expected = pd.read_sql_query(
            'SELECT * FROM weather ORDER BY id DESC LIMIT 10', conn
        )
        conn.close()
        df_expected.columns = [
            'ID', 'Температура, °C', 'Давление, мм рт. ст.',
            'Скорость ветра, м/с', 'Направление ветра',
            'Количество осадков (дождь), мм', 'Количество осадков (снег), мм'
        ]
        pd.testing.assert_frame_equal(df, df_expected, check_dtype=False)


if __name__ == '__main__':
    unittest.main()
