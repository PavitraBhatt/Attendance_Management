from rest_framework import serializers
from .models import HR,Department

class HRSerializer(serializers.Serializer):
    HRID = serializers.CharField(max_length=100)
    FirstName = serializers.CharField(max_length=100)
    MiddleName = serializers.CharField(max_length=100)
    LastName = serializers.CharField(max_length=100)
    Password = serializers.CharField(max_length=100)
    Email = serializers.EmailField()
    Mobile = serializers.IntegerField()
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
    # DepartmentID = serializers.ForeignKey(Department, on_delete = serializers.CASCADE)
    TimeZone = serializers.CharField(max_length=100)
    JoiningDate = serializers.DateField()
    AboutMe = serializers.CharField(max_length=100)
    Photo = serializers.ImageField()
    LegalDocument = serializers.ImageField()

    DepartmentID = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = HR
        fields = '__all__'  # Include all fields from the Employee model