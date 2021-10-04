from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'viz/viz_main.html')

def map(request):
    return render(request, 'viz/viz_map.html')

def chart_gender(request):
    return render(request, 'viz/viz_gender.html')