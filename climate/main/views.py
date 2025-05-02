from django.shortcuts import render
import requests
from django.conf import settings
import json

def index(request):
    api = settings.WEATHER_API_KEY
    result = {}
    if request.method == 'POST':
        city = request.POST['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
        response = requests.get(url)
        print(response.json())
        result = response.json()


    return render(request, 'index.html', {"data": result })
