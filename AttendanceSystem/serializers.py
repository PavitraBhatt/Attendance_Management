from rest_framework import serializers
from .models import Attendance

# Create your serializers here.

class AttendanceSerializer(serializers.Serializerl):
    photo = serializers.ImageField()
    Date = serializers.DateField()
    Latitude = serializers.FloatField()
    Longtitude = serializers.FloatField()

    class Meta:
        model = Attendance
        fields = '__all__'  # Include all fields from the Employee model