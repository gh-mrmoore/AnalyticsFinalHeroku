from django.urls import path
from . import views

app_name = 'dash'
urlpatterns = [
    path('', views.index, name='index'),
    # home urls
    path('home/purpose', views.purpose, name='purpose'), 
    path('home/communications', views.comms, name='comms'), 
    path('home/team', views.team, name='team'), 
    # data urls
    path('data', views.data, name='data'), 
    # models urls
    path('models', views.models, name='models'), 
    path('background', views.background, name='background'), 
    # charts urls
    path('charts', views.charts, name='charts'), 
    path('charts/gender', views.chart_gender, name='chart_gender'), 
]