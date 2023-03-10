from .models import Forecast
from rest_framework import serializers


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ('id', 'city', 'state', 'notes',)