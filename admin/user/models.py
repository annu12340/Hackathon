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

class UserDetails(models.Model):
    userid = models.IntegerField()
    name = models.CharField(max_length=120)
    blood_group = models.CharField(max_length=10)

    def __str__(self):
        return "User "+str(self.userid)
