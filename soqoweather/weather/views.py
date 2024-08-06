import logging, json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .db_conn import SessionLocal
from .models import Weather
from .serializers import WeatherSerializers

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


class WeatherAPICreateView(APIView):
    def post(self, request):
        try:
            serializer = WeatherSerializers(data=request.data)
            if serializer.is_valid():
                saved_weather_data = serializer.save()
                logging.info('New data persisted with ID: {}'.format(saved_weather_data.id))
                response_data = {'id': saved_weather_data.id}
                return Response(response_data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logging.error(f"An error occurred: {str(ex)}")
            error = {'Error message': str(ex)}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WeatherAPIFetchView(APIView):

    def get(self, request, city):
        try:
            session = SessionLocal()
            weather_data = session.query(Weather).filter_by(city=city).all()
            session.close()

            if not weather_data:
                logging.warning("No data found for %s" % city)
                return Response("No data found for %s" % city, status.HTTP_404_NOT_FOUND)

            serializer = WeatherSerializers(weather_data, many=True)
            logging.info("Data found for %s: %s" % (city, serializer.data))
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            logging.error(f"An error occurred: {str(ex)}")
            error = {'Error message': str(ex)}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
