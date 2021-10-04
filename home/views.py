from django.shortcuts import render

# Views for the home area
def index(request):
    return render(request, 'home/home_main.html')

def purpose(request):
    return render(request, 'home/home_purpose.html')

def comms(request):
    return render(request, 'home/home_comms.html')

def team(request):
    return render(request, 'home/home_team.html')
