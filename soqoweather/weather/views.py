from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .db_conn import SessionLocal
from .models import Weather
from .serializers import WeatherSerializers


class WeatherAPICreateView(APIView):
    def post(self, request):
        serializer = WeatherSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeatherAPIFetchView(APIView):

    def get(self, request, city):
        session = SessionLocal()
        weather_data = session.query(Weather).filter_by(city=city).all()
        session.close()

        if not weather_data:
            return Response("No data found for %s" % city, status.HTTP_404_NOT_FOUND)

        serializer = WeatherSerializers(weather_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)