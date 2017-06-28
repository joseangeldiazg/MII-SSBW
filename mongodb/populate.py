from mongoengine import *
from requests import *
import datetime

db=connect('test')
db.drop_database('test')

#Borramos la base de datos para que no se pisen los documentos


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

def obtenerRestaurantes(bar, city, cuisine, borough, id):
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address='
    url = url+bar+city
    response = get(url)
    data = parseDireccion(response.json());
    dir = addr(building = data['number'] , street=data['street'], city=data['city'], zipcode=data['postal_code'], coord=[data['latitude'], data['longitude']])
    r = restaurants(name=bar, restaurant_id=id, cuisine=cuisine, borough=borough, address=dir)
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

obtenerRestaurantes("Casa Julio", "Granada", "Granaina", "Centro", 1)
obtenerRestaurantes("El Nido del Búho", "Granada", "Tapas", "Plaza de Toros", 2)
obtenerRestaurantes("Pizzametro", "Granada", "Italiana", "Centro", 3)
obtenerRestaurantes("La Bodeguica de Miguel del Rei", "Almería", "Tapas", "San Luís", 4)

obtenerRestaurantes("Casa Julio", "Granada", "Granaina", "Centro", 5)
obtenerRestaurantes("El Nido del Búho", "Granada", "Tapas", "Plaza de Toros", 6)
obtenerRestaurantes("Pizzametro", "Granada", "Italiana", "Centro", 7)
obtenerRestaurantes("La Bodeguica de Miguel del Rei", "Almería", "Tapas", "San Luís", 8)


    #ne – not equal to
    #lt – less than
    #lte – less than or equal to
    #gt – greater than
    #gte – greater than or equal to
    #not – negate a standard check, may be used before other operators (e.g. Q(age__not__mod=5))
    #in – value is in list (a list of values should be provided)
    #nin – value is not in list (a list of values should be provided)
    #mod – value % x == y, where x and y are two provided values
    #all – every item in list of values provided is in array
    #size – the size of the array is
    #exists – value for field exists


# Consulta, los tres primeros
for r in restaurants.objects[:3]:
    print (r.name, r.cuisine, r.address.street, r.address.coord)

#Consultar por tipo de cocina tapas
for r in restaurants.objects(cuisine="Tapas"):
    print (r.name)

#Consultar por tipo de cocina no tapas
for r in restaurants.objects(cuisine__ne="Tapas"):
    print (r.name)

#Consultar por geolocalizacion.

for r in restaurants.objects(address__coord__within_distance=[(37.18, -3.60), 1]):
    print (r.name)
