from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse   
import io
from rest_framework.parsers import JSONParser
from .serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

def employee_detail(request,pk):
    # return HttpResponse("Hrllo")
    emp = Employee.objects.get(id = pk)
    serializer = EmployeeSerializer(emp)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(serializer.data)

def employee_list(request):
    # return HttpResponse("Hrllo")
    emp = Employee.objects.all()
    serializer = EmployeeSerializer(emp, many = True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)


class EmployeeCreateView(APIView):
    def post(self, request):
        json_data = request.data
        serializer = EmployeeSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Employee Created Successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
class EmployeeGetView(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        if id is not None:
            try:
                emp = Employee.objects.get(id=id)
                serializer = EmployeeSerializer(emp)
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            emp = Employee.objects.all()
            serializer = EmployeeSerializer(emp, many=True)
            return Response(serializer.data)


class EmployeeGetIdView(APIView):
    def get(self, request, EmployeeID=None):
        if EmployeeID is not None:
            try:
                emp_obj = Employee.objects.get(EmployeeID=EmployeeID)  # Assuming 'EmployeeID' is the field name
                serializer = EmployeeSerializer(emp_obj)
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)
    
class EmployeePostView(APIView):
    def post(self, request):
        json_data = request.data
        serializer = EmployeeSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Employee Created Successfully!'}
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class EmployeeUpdateView(APIView):
    def get_object(self, EmployeeID):
        try:
            return Employee.objects.get(EmployeeID=EmployeeID)
        except Employee.DoesNotExist:
            return None

    def post(self, request, EmployeeID):
        emp_obj = self.get_object(EmployeeID)
        if emp_obj is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(emp_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class EmployeePutView(APIView):
    def put(self, request):
        json_data = request.data

        if isinstance(json_data, list):
            # Handle the case of updating multiple employees
            response_data = {'msg': 'Updating multiple employees'}
            for data in json_data:
                employee_id = data.get('EmployeeID')
                try:
                    emp = Employee.objects.filter(EmployeeID=employee_id)
                    if emp.exists():
                        for emp_obj in emp:
                            serializer = EmployeeSerializer(emp_obj, data=data, partial=True)
                            if serializer.is_valid():
                                serializer.save()
                            else:
                                response_data = {'error': serializer.errors}
                    else:
                        response_data = {'error': f'No employee found with EmployeeID {employee_id}'}
                except Exception as e:
                    response_data = {'error': str(e)}
        else:
            # Handle the case of updating a single employee
            employee_id = json_data.get('EmployeeID')
            try:
                emp = Employee.objects.filter(EmployeeID=employee_id)
                if emp.exists():
                    for emp_obj in emp:
                        serializer = EmployeeSerializer(emp_obj, data=json_data, partial=True)
                        if serializer.is_valid():
                            serializer.save()
                        else:
                            response_data = {'error': serializer.errors}
                else:
                    response_data = {'error': f'No employee found with EmployeeID {employee_id}'}
            except Exception as e:
                response_data = {'error': str(e)}
        
        return Response(response_data)


class EmployeeDeleteView(APIView):
    def delete(self, request):
        json_data = request.data
        EmployeeID = json_data.get('EmployeeID')

        try:
            emp = Employee.objects.get(EmployeeID=EmployeeID)
            emp.delete()
            res = {'msg': f"Employee is deleted with the EmployeeID: {EmployeeID}"}
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        except Employee.DoesNotExist:
            res = {'error': 'Employee not found'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)