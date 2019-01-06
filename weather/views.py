from django.shortcuts import render
import requests
from .models import City

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9c0c4ad1549fe55a212bd50fd12e3047'
    city = "Memphis"

    cities = City.objects.all()
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': r['name'],
            'temperature': r['main']['temp'],
            'description':r["weather"][0]['description'] ,
            'icon': r['weather'][0]['icon']

        }
        weather_data.append(city_weather)


    context = {'city_weather': city_weather}
    #print(city_weather)
    return render(request,'weather/weather.html',context)
