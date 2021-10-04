from django.urls import path
from . import views

app_name = 'dash'
urlpatterns = [
    path('', views.index, name='index'),
    # home urls
    # data urls
    path('data', views.data, name='data'), 
    # charts urls
    path('viz', views.charts, name='charts'), 
    path('viz/map', views.map, name='map'), 
    path('viz/gender', views.chart_gender, name='chart_gender'), 
]