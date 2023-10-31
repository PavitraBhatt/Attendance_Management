from .models import Employee,Department
from rest_framework import serializers
from Site.serializers import Site
# Create your serializers here.


class EmployeeSerializer(serializers.Serializer):
    EmployeeID = serializers.CharField(max_length=100)
    FirstName = serializers.CharField(max_length=100)
    MiddleName = serializers.CharField(max_length=100)
    LastName = serializers.CharField(max_length=100)
    Password = serializers.CharField(max_length=100)
    Email = serializers.EmailField()
    Mobile = serializers.IntegerField() #we can add check constaints
    DOB = serializers.DateField()
    HouseNumber = serializers.CharField(max_length=100) 
    ApartmentNumber = serializers.CharField(max_length=100)
    Landmark = serializers.CharField(max_length=100)
    City = serializers.CharField(max_length=100)
    State =  serializers.CharField(max_length=100)
    PIN = serializers.IntegerField()
    BloodGroup = serializers.CharField(max_length=100)
    NickName = serializers.CharField(max_length=100)
    EmergencyNumber = serializers.IntegerField()
    MatrialStatus = serializers.CharField(max_length=100)
    # DepartmentID = serializers.ForeignKey(Department, on_delete=serializers.CASCADE,null=True)
    TimeZone = serializers.CharField(max_length=100)
    JoiningDate = serializers.DateField()
    AboutMe = serializers.CharField(max_length=100)
    Photo = serializers.ImageField()
    LegalDocument = serializers.ImageField()
    Designation = serializers.CharField(max_length=100)
    # SiteID = serializers.ForeignKey(Site,on_delete=serializers.CASCADE,null=True)

    DepartmentID = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    SiteID = serializers.PrimaryKeyRelatedField(queryset=Site.objects.all())

    class Meta:
        model = Employee
        fields = '__all__'  # Include all fields from the Employee model
    