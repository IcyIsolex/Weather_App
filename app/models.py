from django.db import models
class City(models.Model):
    cityname=models.CharField(max_length=25)
    def __str__(self):
        return self.cityname