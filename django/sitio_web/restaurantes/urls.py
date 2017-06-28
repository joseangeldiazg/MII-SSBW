from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^listar/$', views.listar, name='listar'),
  url(r'^listar/introducir/$', views.introducir, name='introducir'),
  url(r'^buscar/introducir/$', views.introducir, name='introducir'),
  url(r'^buscar/$', views.buscar, name='buscar'),
    url(r'^restaurant/(?P<id>[0-9]+)$', views.restaurant, name='restaurant'),
]
