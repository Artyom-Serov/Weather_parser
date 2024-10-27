import unittest
import aiohttp
import asyncio
from aioresponses import aioresponses
from core.requests import get_weather, API_URL

class TestWeatherRequests(unittest.IsolatedAsyncioTestCase):
    async def test_get_weather_success(self):
        """Тест успешного выполнения асинхронного запроса к OpenWeather API."""
        mock_response = {
            "main": {
                "temp": 22.5,
                "pressure": 1012
            },
            "wind": {
                "speed": 3.5,
                "deg": 180
            },
            "rain": {
                "1h": 0.2
            },
            "snow": {
                "1h": 0
            }
        }

        with aioresponses() as m:
            m.get(API_URL, payload=mock_response)
            weather_data = await get_weather()

            self.assertIsNotNone(weather_data)
            self.assertEqual(weather_data["temperature"], 22.5)
            self.assertEqual(weather_data["pressure"], 1012)
            self.assertEqual(weather_data["wind_speed"], 3.5)
            self.assertEqual(weather_data["wind_deg"], 180)
            self.assertEqual(weather_data["rain"], 0.2)
            self.assertEqual(weather_data["snow"], 0)

    async def test_get_weather_timeout(self):
        """Тест обработки ошибки тайм-аута при запросе к API."""
        with aioresponses() as m:
            m.get(API_URL, exception=asyncio.TimeoutError)
            weather_data = await get_weather()

            self.assertIsNone(weather_data)

    async def test_get_weather_client_error(self):
        """Тест обработки ошибки соединения при запросе к API."""
        with aioresponses() as m:
            m.get(API_URL, exception=aiohttp.ClientError)
            weather_data = await get_weather()

            self.assertIsNone(weather_data)


if __name__ == '__main__':
    unittest.main()
