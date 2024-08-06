from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import WeatherTest


class WeatherAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.weather_data = {
            "city": "Rome",
            "date": "2024-07-07",
            "temperature": 4.4,
            "description": "Winter"
        }
        self.create_url = reverse('create-weather')
        self.get_url = reverse('get-weather', args=['Rome'])
        self.get_url_wrong_city = reverse('get-weather', args=['Lost City'])

        self.weather = WeatherTest("Rome", "2024-07-07", 4.4, "Winter")

    def test_create_weather(self):
        response = self.client.post(self.create_url, self.weather_data, format='json')
        """Assert that status code is 201"""
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_weather(self):
        response = self.client.get(self.get_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['city'], self.weather.city)
        self.assertEqual(response.data[0]['temperature'], self.weather.temperature)

    def test_get_weather_wrong_data(self):
        response = self.client.get(self.get_url_wrong_city)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, "No data found for Lost City")
