from rest_framework import serializers
from .models import Site
class SiteSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    SiteID = serializers.CharField(max_length=100)
    Address1 = serializers.CharField(max_length=100)
    Address1 = serializers.CharField(max_length=100)
    City = serializers.CharField(max_length=100)
    State =  serializers.CharField(max_length=100)
    PIN = serializers.IntegerField()
    Latitude = serializers.FloatField()
    Longtitude = serializers.FloatField()

    def create(self,validate_data):
        return Site.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        print(instance.SiteID) #give old data(SiteID)
        instance.SiteID = validated_data.get('SiteID',instance.SiteID)
        print(instance.SiteID) #give new pdated data(SiteID)
        instance.Address1 = validated_data.get('Address1',instance.Address1)
        instance.Address2 = validated_data.get('Address2',instance.Address2)
        instance.City = validated_data.get('City',instance.City)
        instance.State = validated_data.get('State',instance.State)
        instance.PIN = validated_data.get('PIN',instance.PIN)
        instance.Latitude = validated_data.get('Latitude',instance.Latitude)
        instance.Longtitude = validated_data.get('Longtitude',instance.Longtitude)
        instance.save()
        return instance