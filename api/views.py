from django.core.serializers import serialize
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView, View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CitySerializer,CityWeatherSerializer
from rest_framework.views import APIView
from main.models import City, CityWeatherInfo
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CityList(APIView):
    authentication_classes = (TokenAuthentication,BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def city_list(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)

class CityDetail(APIView):
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        city_name = request.data.get('city_name')

        if not city_name:
            return Response({'error': 'city_name is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            city_name = city_name.strip().lower()
            city = City.objects.get(name__iexact=city_name)

            latest_weather = CityWeatherInfo.objects.filter(city=city).order_by('-TimeStamp').first()

            if not latest_weather:
                return Response({'error': 'No weather data available for this city'}, status=status.HTTP_404_NOT_FOUND)

            serializer = CityWeatherSerializer(latest_weather)
            return Response(serializer.data)

        except City.DoesNotExist:
            return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)
