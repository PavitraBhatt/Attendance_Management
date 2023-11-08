from django.shortcuts import render
from rest_framework.views import APIView
from AttendanceSystem.serializers import AttendanceSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from AttendanceSystem.models import Attendance
from django.http import JsonResponse,HttpResponse   
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
# Create your views here.

class AttendenceCreateView(APIView):
    def post(self, request):
        json_data = request.data
        serializer = AttendanceSerializer(data=json_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class AttendanceGetIdView(APIView):
    @csrf_exempt
    def get(self, request, id=None):
        if id is not None:
            try:
                attendance_obj = Attendance.objects.get(id=id)  # Change variable name to "attendance_obj"
                serializer = AttendanceSerializer(attendance_obj)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except Attendance.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        attendance = Attendance.objects.all()  # Change variable name to "attendance"
        serializer = AttendanceSerializer(attendance, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')



class AttendanceUpdateView(APIView):
    @csrf_exempt
    def get_object(self, id):
        try:
            return Attendance.objects.get(id=id)
        except Attendance.DoesNotExist:
            return None

    def get(self, request, id):
        Attendance_obj = self.get_object(id)
        if Attendance_obj is None:
            return Response(status=500)
        serializer = AttendanceSerializer(Attendance_obj)
        return JsonResponse(serializer.data)

    def post(self, request, id):
        Attendance_obj = self.get_object(id)
        if Attendance_obj is None:
            return Response(status=400)

        data = JSONParser().parse(request)
        serializer = AttendanceSerializer(Attendance_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=405)
    

class AttendanceDeleteView(APIView):
    def delete(self, request):
        data = request.data
        id = data.get('id')

        try:
            Attendance = Attendance.objects.get(id = id)
            Attendance.delete()
            res = {'msg': f'Attendance is deleted with the AttendanceID: {id}'}
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        except Attendance.DoesNotExist:
            res = {'error': 'Attendance not found'}
            return JsonResponse(res, safe=False, status=status.HTTP_404_NOT_FOUND)