# url paths for viz django app

from django.urls import include, path
from . import views

app_name = 'viz'

urlpatterns = [
    path('', views.home, name='home'), 
    path('map', views.map, name='map'), 
    path('gender', views.chart_gender, name='chart_gender'), 
]