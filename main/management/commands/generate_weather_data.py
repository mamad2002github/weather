import random
from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from main.models import City, CityWeatherInfo
class Command(BaseCommand):
    help = 'Generate weather data'

    def handle(self, *args, **options):
        for city in City.objects.all():
            for i in range(5):
                days_ago = random.randint(0, 365)
                TimeStamp = now() - timedelta(days=days_ago)
                temperature = round(random.uniform(-10, 40), 2)
                CityWeatherInfo.objects.create(city=city, Temperature=temperature, TimeStamp=TimeStamp)
            self.stdout.write(self.style.SUCCESS('Weather data generated successfully.'))