from django.db import models
from Department.models import Department
from Site.models import Site
# Create your models here.


class Employee(models.Model):
    EmployeeID = models.CharField(max_length=100,primary_key=True)
    FirstName = models.CharField(max_length=100)
    MiddleName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Email = models.EmailField()
    Mobile = models.IntegerField() #we can add check constaints
    DOB = models.DateField()
    HouseNumber = models.CharField(max_length=100) 
    ApartmentNumber = models.CharField(max_length=100)
    Landmark = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State =  models.CharField(max_length=100)
    PIN = models.IntegerField()
    BloodGroup = models.CharField(max_length=100)
    NickName = models.CharField(max_length=100)
    EmergencyNumber = models.IntegerField()
    MatrialStatus = models.CharField(max_length=100)
    DepartmentID = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    TimeZone = models.CharField(max_length=100)
    JoiningDate = models.DateField()
    AboutMe = models.CharField(max_length=100)
    Photo = models.ImageField()
    LegalDocument = models.ImageField()
    Designation = models.CharField(max_length=100)
    SiteID = models.ForeignKey(Site,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.EmployeeID
    