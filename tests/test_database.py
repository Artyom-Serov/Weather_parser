import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.models import Base, Weather
from core.database import save_weather_to_db


class TestDatabase(unittest.TestCase):
    def setUp(self):
        """Создание временной базы данных для тестирования."""
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def tearDown(self):
        """Очистка базы данных после каждого теста."""
        Base.metadata.drop_all(self.engine)

    def test_save_weather_to_db(self):
        """Тестирование сохранения данных о погоде в базу."""
        weather_data = {
            "temperature": 20.5,
            "pressure": 1013,
            "wind_speed": 5.5,
            "wind_deg": 270,
            "rain": 0,
            "snow": 2
        }
        session = self.Session()
        save_weather_to_db(weather_data, session=session)
        weather_entry = session.query(Weather).first()

        self.assertEqual(weather_entry.temperature, 20)
        self.assertEqual(weather_entry.pressure, 760)
        self.assertEqual(weather_entry.wind_deg, 'З')

        self.assertEqual(weather_entry.wind_speed, 5.5)
        self.assertEqual(weather_entry.rain, 0)
        self.assertEqual(weather_entry.snow, 2)

        session.close()


if __name__ == '__main__':
    unittest.main()
