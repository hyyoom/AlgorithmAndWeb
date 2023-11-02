from rest_framework import serializers
from .models import Weather



class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'



# class Weather(models.Model):
#     temp = models.FloatField()
#     feels_like = models.FloatField()
#     dt_txt = models.DateTimeField()

    