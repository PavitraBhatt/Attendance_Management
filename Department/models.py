from django.db import models

# Create your models here.

class Department(models.Model):
    DepartmentID = models.IntegerField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)
    DepartmentHead = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.DepartmentID