from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50)
    Longitude = models.DecimalField(max_digits=10, decimal_places=2)
    Latitude = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class CityWeatherInfo(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    Temperature = models.FloatField()
    TimeStamp = models.DateTimeField()
    def __str__(self):
        return f'{self.city.name}'