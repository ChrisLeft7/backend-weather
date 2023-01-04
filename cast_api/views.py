from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
from rest_framework.response import Response
from rest_framework.decorators import api_view

load_dotenv()

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

@api_view(['GET'])
def weather(request, city):
    API_KEY = os.getenv('API_KEY')
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial'
    data = requests.get(api_url).json()
    return Response(data)
