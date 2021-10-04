from django.shortcuts import render

# Create your views here.
def ml_main(request):
    return render(request, 'mlmodels/mlmodel_main.html')

def model01(request):
    return render(request, 'mlmodels/mlmodel_model01.html')

def model02(request):
    return render(request, 'mlmodels/mlmodel_model02.html')

def model03(request):
    return render(request, 'mlmodels/mlmodel_model03.html')

def model03a(request):
    return render(request, 'mlmodels/mlmodel_model03a.html')