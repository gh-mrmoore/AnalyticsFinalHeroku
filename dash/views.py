from django.shortcuts import render

# Create your views here.

def background(request):
    return render(request, 'background/background.html')


# views for the data area
def data(request):
    return render(request, 'data/data_main.html')

# views for the visualizations area
def charts(request):
    return render(request, 'viz/viz_main.html')

def map(request):
    return render(request, 'viz/viz_map.html')

def chart_gender(request):
    return render(request, 'viz/viz_gender.html')