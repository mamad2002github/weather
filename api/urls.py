from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("cities",views.CityList.as_view()),
    path("weather/",views.CityDetail.as_view()),
    path("api-token",obtain_auth_token),
]