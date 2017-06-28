from django.shortcuts import render, HttpResponse
from .models import restaurants
from .forms import AddRestaurant

# Create your views here.

def handle_uploaded_file(n, f):
    with open('static/img/restaurants/' + str(n) + '.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

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

def add(request):
    if request.method == "POST":
        form = AddRestaurant(request.POST, request.FILES)
        if form.is_valid():
            if len(request.FILES) != 0:
                handle_uploaded_file(restaurants.objects.count() + 1, request.FILES['image'])
            r = form.save()
            return redirect('listar')
    else:
        form = AddRestaurant();
    # GET o error
    context = {
        'form': form,
    }
    return render(request, 'restaurantes/addrestaurant.html', context)

def restaurant(request, id):
    restaurante = restaurants.objects(restaurant_id=id)[0]
    context = {
            "resta": restaurante,
            "imagen": str(restaurante.restaurant_id)
    }
    return render (request, 'restaurantes/restaurant.html', context)

def buscar(request):
    parametro=request.GET.get('zona')
    context={
        "resta":restaurants.objects(borough=parametro)
    }
    return render (request, 'restaurantes/listar.html', context)
