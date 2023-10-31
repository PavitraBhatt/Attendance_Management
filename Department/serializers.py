from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.Serializer):
    DepartmentID = serializers.IntegerField()
    DepartmentName = serializers.CharField(max_length=100)
    DepartmentHead = serializers.CharField(max_length=100)

    class Meta:
        model = Department
        fields = '__all__'  # Include all fields from the Employee model

    def create(self,validate_data):
        return Department.objects.create(**validate_data)
    
    # def update(self, instance, validated_data):
    #     print(instance.DepartmentID) #give old data(DepartmentID)
    #     instance.DepartmentID = validated_data.get('DepartmentID',instance.DepartmentID)
    #     print(instance.DepartmentID) #give new pdated data(DepartmentID)
    #     instance.HouseNumber = validated_data.get('HouseNumber',instance.HouseNumber)
    #     instance.ApartmentNumber= validated_data.get('ApartmentNumber',instance.ApartmentNumber)
    #     instance.Landmark = validated_data.get('LandMark',instance.Landmark)
    #     instance.City = validated_data.get('City',instance.City)
    #     instance.State = validated_data.get('State',instance.State)
    #     instance.PIN = validated_data.get('PIN',instance.PIN)
    #     instance.Latitude = validated_data.get('Latitude',instance.Latitude)
    #     instance.Longtitude = validated_data.get('Longtitude',instance.Longtitude)
    #     instance.save()
    #     return instance
    
    def update(self, instance, validated_data):
        # Implement the logic to update the instance based on the validated data
        # and return the updated instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance