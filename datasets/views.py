from django.shortcuts import render

# Create your views here.
def data_main(request):
    return render(request, 'datasets/datasets_main.html')