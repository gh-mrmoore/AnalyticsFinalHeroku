from django.shortcuts import render

# Create your views here.

def background(request):
    return render(request, 'dash/background.html')

# view for the home area
def index(request):
    return render(request, 'dash/home_intro.html')

def purpose(request):
    return render(request, 'dash/home_purpose.html')

def comms(request):
    return render(request, 'dash/home_comms.html')

def team(request):
    return render(request, 'dash/home_team.html')

# views for the model area
def models(request):
    return render(request, 'models/models_main.html')

# views for the data area
def data(request):
    return render(request, 'data/data_main.html')

# views for the charts area
def charts(request):
    return render(request, 'charts/charts_main.html')

def chart_gender(request):
    return render(request, 'charts/charts_gender.html')