from django.shortcuts import render, HttpResponse
from .models import restaurants
# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)

def listar(request):
    context = {
            "resta": restaurants.objectcs.all, # los cinco primeros
         }
    return render (requests, 'restaurantes/listar.html', context)
