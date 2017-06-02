from django.shortcuts import render, HttpResponse
from .models import restaurants
# Create your views here.

def index(request):
    context = {
            "resta": restaurants.objects[:5], # los cinco primeros
         }
    return render (request, 'restaurantes/listar.html', context)

def listar(request):
    context = {
            "resta": restaurants.objects[:2], # los cinco primeros
         }
    return render (request, 'restaurantes/listar.html', context)

def introducir(request):
    return render (request, 'restaurantes/introducir.html')

def buscar(request):
    parametro=request.GET.get('zona')
    context={
        "resta":restaurants.objects(borough=parametro)
    }
    return render (request, 'restaurantes/listar.html', context)
