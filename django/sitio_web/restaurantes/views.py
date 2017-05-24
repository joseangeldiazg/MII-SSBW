from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)
