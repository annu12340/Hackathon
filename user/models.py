from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Appointments(models.Model):
    patientid = models.IntegerField()
    patientname = models.CharField(max_length=120)
    doctorid = models.IntegerField()
    doctorurl = models.CharField(max_length=120)
    datetime = models.DateTimeField()
    type = models.CharField(max_length=80)
    amount = models.IntegerField()

    def __str__(self):
        return "patient "+str(self.patientid)+" doctor "+str(self.doctorid)

class Details(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class CulpritDetails(models.Model):
    age = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    eyes = models.CharField(max_length=100)
    skin = models.CharField(max_length=100)
    facial_features   = models.CharField(max_length=100)
    physcial_features  = models.CharField(max_length=100)
    other_details  = models.CharField(max_length=100)
    def __str__(self):
        return self.name