from rest_framework import serializers
from .db_conn import SessionLocal
from .models import Weather


class WeatherSerializers(serializers.Serializer):
    city = serializers.CharField(max_length=100)
    date = serializers.DateField()
    temperature = serializers.FloatField()
    description = serializers.CharField()

    def create(self, weather_data):
        session = SessionLocal()
        weather = Weather(**weather_data)
        session.add(weather)
        session.commit()
        session.refresh(weather)
        session.close()
        return weather
