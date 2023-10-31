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

@csrf_exempt
def employee_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Employee Created Succesfully !'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        else :
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type= 'application/json')

@csrf_exempt       
def employee_get(request): 
    
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        decoded_data = stream.getvalue().decode('utf-8')
        pythondata = json.dumps(decoded_data)
        # id = pythondata.get('id',None)
        id = pythondata.get('id', None) if isinstance(pythondata, dict) else None

        if id is not None:
            site = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(site)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type ='application/json')
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type ='application/json')

@csrf_exempt
def employee_get_id(request, EmployeeID=None):  # Accept the 'EmployeeID' parameter
    
    if request.method == 'GET':
        if EmployeeID is not None:
            try:
                emp_obj = Employee.objects.get(EmployeeID=EmployeeID)  # Assuming 'EmployeeID' is the field name
                serializer = EmployeeSerializer(emp_obj)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except Employee.DoesNotExist:
                return HttpResponse(status=404)
        
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
@csrf_exempt
def employee_post(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer =EmployeeSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Employee Created Succesfully !'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json', status = status.HTTP_201_CREATED)  
        else :
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json')
        
# @csrf_exempt
# def employee_put(request):
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         employee_id = pythondata.get('EmployeeID')
#         # emp = Employee.objects.filter(EmployeeID=employee_id)
#         # serializer = EmployeeSerializer(employee,data = pythondata, partial = True) #if partial =False you write then we have give full information fully update
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     res = {'msg':'data updated'}
#         #     json_data = JSONRenderer().render(res)
#         #     return HttpResponse(json_data,content_type = 'application/json')
        
#         # else:
#         #     json_data = JSONRenderer().render(serializer.errors)
#         #     return HttpResponse(json_data,content_type = 'application/json')
#         try:
#             emp = Employee.objects.filter(EmployeeID=employee_id)
#             if emp.exists():
#                 # Update the attributes of each site in the queryset
#                 for emp in emp:
#                     serializer = EmployeeSerializer(emp, data=pythondata, partial=True)
#                     if serializer.is_valid():
#                         serializer.save()
#                 response_data = {'msg': 'Data updated'}
#             else:
#                 response_data = {'error': 'No employee found with the given EmployeeID'}
#         except :
#             response_data = {'error': 'Employee does not exist'}
        
#         return JsonResponse(response_data)

@csrf_exempt
def employee_update(request, EmployeeID):
    try:
        emp_obj = Employee.objects.get(EmployeeID=EmployeeID)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(emp_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def employee_put(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
     
        if isinstance(pythondata, list):
            # Handle the case of updating multiple employees
            response_data = {'msg': 'Updating multiple employees'}
            for data in pythondata:
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
            employee_id = pythondata.get('EmployeeID')
            try:
                emp = Employee.objects.filter(EmployeeID=employee_id)
                if emp.exists():
                    for emp_obj in emp:
                        serializer = EmployeeSerializer(emp_obj, data=pythondata, partial=True)
                        if serializer.is_valid():
                            serializer.save()
                        else:
                            response_data = {'error': serializer.errors}
                else:
                    response_data = {'error': f'No employee found with EmployeeID {employee_id}'}
            except Exception as e:
                response_data = {'error': str(e)}
        
        return JsonResponse(response_data)

@csrf_exempt
def employee_delete(request):       
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        EmployeeID = pythondata.get('EmployeeID')
        # emp = Employee.objects.get(EmployeeID=EmployeeID)
        # emp.delete()
        # res={'msg':'Data Deleted'}
        try:
            emp = Employee.objects.get(EmployeeID=EmployeeID)
            emp.delete()
            res = {'msg': f"Employee is deleted with the EmployeeID : {EmployeeID}"}
        except :
            res = {'error': 'Employee not found'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type = 'application/json')
        return JsonResponse(res,safe=False,status = status.HTTP_204_NO_CONTENT)