from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .serializers import WeatherSerializers
from .models import Weather

# Create your views here.

@api_view(['GET'])
def index(request):
    api_key = '5310463b07693b401bc5cb3c5967c297'
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(url).json()

    return Response(response)


@api_view(['GET'])
def save_data(request):
    api_key = '5310463b07693b401bc5cb3c5967c297'
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(url).json()

    for li in response.get("list"):
        save_data = {
            'dt_txt' : li.get('dt_txt'),
            'temp' : li.get('main').get('temp'),
            'feels_like' : li.get('main').get('feels_like'),
        }
        serializer = WeatherSerializers(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # return Response(serializer.data)
    return JsonResponse({'message' : 'okay'})



@api_view(['GET'])
def list_data(request):
    weathers = Weather.objects.all()
    serializer = WeatherSerializers(weathers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def hot_weathers(request):
    weathers = Weather.objects.all()

    hot_weathers = []
    for weather in weathers:
        tmp = round(weather.temp - 273.15, 2)
        if tmp > 0:
            hot_weathers.append(weather)
    
    serializer = WeatherSerializers(hot_weathers, many=True)
    return Response(serializer.data, status=200)
    

