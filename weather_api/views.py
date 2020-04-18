from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    cities = City.objects.all() #return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b292883e5301964b10083b3014f2c41e'

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    forecast = []

    for city in cities:

        city_forecast = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_forecast['main']['temp'],
            'description' : city_forecast['weather'][0]['description'],
            'icon' : city_forecast['weather'][0]['icon']
        }

        forecast.append(weather) #add the data for the current city into our list

    context = {'forecast' : forecast, 'form' : form}

    return render(request, 'weather_api/index.html', context) #returns the index.html template

