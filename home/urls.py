from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'), 
    path('purpose', views.purpose, name='purpose'), 
    path('communications', views.comms, name='comms'), 
    path('team', views.team, name='team'), 
]