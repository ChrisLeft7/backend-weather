from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

# Create your views here.
from rest_framework import generics
from .serializers import ForecastSerializer
from .models import Forecast

class ForecastList(generics.ListCreateAPIView):
    queryset = Forecast.objects.all().order_by('city')
    serializer_class = ForecastSerializer

class ForecastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forecast.objects.all().order_by('city')
    serializer_class = ForecastSerializer

def weather(request):
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q=Chicago&appid={API_KEY}&units=imperial'
    response = requests.get(api_url)
    data = response.json()

    print(data)