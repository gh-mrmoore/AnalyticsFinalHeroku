from django.urls import path
from . import views

app_name = 'datasets'
urlpatterns = [
    path('', views.data_main, name='data_main'), 
    # path('/traff_data', views.traff_data, name='traff_data'), 

]