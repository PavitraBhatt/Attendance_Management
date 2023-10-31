from django.db import models

# Create your models here.

class Site(models.Model):
    SiteID = models.CharField(max_length=100,primary_key=True)
    Address1 = models.CharField(max_length=100)
    Address2 = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State =  models.CharField(max_length=100)
    PIN = models.IntegerField()
    Latitude = models.FloatField()
    Longtitude = models.FloatField()
    # PHOTO

    def __str__(self):
        return self.SiteID