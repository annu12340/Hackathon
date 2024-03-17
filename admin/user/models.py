from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Details(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class CulpritDetails(models.Model):
    details = models.CharField(max_length=100)

    
class ShelterHome(models.Model):
    name =  models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    max_capacity = models.IntegerField()
    current_capacity = models.IntegerField()
    remaining_capacity = models.IntegerField()
