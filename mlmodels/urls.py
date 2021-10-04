from django.urls import path
from . import views

app_name = 'mlmodels'
urlpatterns = [
    path('', views.ml_main, name='ml_main'), 
    path('model01', views.model01, name='model01'), 
    path('model02', views.model01, name='model02'), 
    path('model03', views.model01, name='model03'), 
    path('model03a', views.model01, name='model03a'), 
]