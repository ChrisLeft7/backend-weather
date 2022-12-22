from django.urls import path
from . import views

urlpatterns = [
    path('api/forecast', views.ForecastList.as_view(), name='forecast_list'),
    path('api/forecast/<int:pk>', views.ForecastDetail.as_view(), name='forecast_detail')
]