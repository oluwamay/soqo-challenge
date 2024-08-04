from django.urls import path
from .views import WeatherAPICreateView, WeatherAPIFetchView

urlpatterns = [
    path('weather', WeatherAPICreateView.as_view(), name='create-weather'),
    path('weather/<str:city>', WeatherAPIFetchView.as_view(), name='get-weather'),
]
