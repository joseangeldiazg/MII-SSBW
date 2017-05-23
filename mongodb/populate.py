from mongoengine import *
from requests import *
import datetime

db=connect('test')

#Borramos la base de datos para que no se pisen los documentos

db.drop_database('test')

# Esquema para la BD de pruebas de mongoDB

class addr(EmbeddedDocument):
    building = StringField()
    street   = StringField()
    city     = StringField()   # añadido
    zipcode  = IntField()
    coord    = GeoPointField() # OJO, al BD de test estan a revés
                               # [long, lat] en vez de [lat, long]

class likes(EmbeddedDocument):
    grade = StringField(max_length=1)
    score = IntField()
    date  = DateTimeField()

class restaurants(Document):
    name             = StringField(required=True, max_length=80)
    restaurant_id    = IntField()
    cuisine          = StringField()
    borough          = StringField()
    address          = EmbeddedDocumentField(addr)              # en la misma collección
    grades           = ListField(EmbeddedDocumentField(likes))


#Vamos a bajar los restaurantes de la api de Google Maps

def obtenerRestaurantes(bar, city, cuisine, borough):
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address='
    url = url+bar+city
    response = get(url)
    data = parseDireccion(response.json());
    dir = addr(building = data['number'] , street=data['street'], city=data['city'], zipcode=data['postal_code'], coord=[data['latitude'], data['longitude']])
    r = restaurants(name=bar, cuisine=cuisine, borough=borough, address=dir)
    r.save()
#Funcion para parsear el restaurante en json

def parseDireccion(json):
    final = {}
    if json['results']:
        data = json['results'][0]
        for item in data['address_components']:
            for category in item['types']:
                data[category] = {}
                data[category] = item['long_name']
        final['number'] = data.get("street_number", None)
        final['street'] = data.get("route", None)
        final['city'] = data.get("locality", None)
        final['postal_code'] = data.get("postal_code", None)
        final['latitude'] = data.get("geometry", {}).get("location", {}).get("lat", None)
        final['longitude'] = data.get("geometry", {}).get("location", {}).get("lng", None)
    return final


dir = addr(street="Hermosa, 5 ", city="Granada", zipcode=18010, coord=[37.1766872, -3.5965171])  # así están bien
r = restaurants(name="Casa Julio", cuisine="Granaina", borough="Centro", address=dir)
r.save()

obtenerRestaurantes("El Nido del Búho", "Granada", "Tapas", "Plaza de Toros")
obtenerRestaurantes("Pizzametro", "Granada", "Italiana", "Centro")
obtenerRestaurantes("La Bodeguica de Miguel del Rei", "Almería", "Tapas", "San Luís")

# Consulta, los tres primeros
for r in restaurants.objects[:2]:
    print (r.name, r.address.coord)

# Hacer más consultas, probar las de geolocalización
# ...
