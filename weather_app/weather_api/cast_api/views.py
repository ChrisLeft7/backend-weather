from django.shortcuts import render

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

