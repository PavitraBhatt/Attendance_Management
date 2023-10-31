from django.db import models

# Create your models here.




class Attendance(models.Model):
    photo = models.ImageField()
    Date = models.DateField()
    Latitude = models.FloatField()
    Longtitude = models.FloatField()

    def __str__(self):
        return self.Date