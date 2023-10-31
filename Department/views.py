from django.shortcuts import render
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse   
import io
from rest_framework.parsers import JSONParser
from .serializers import DepartmentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status

# Create your views here.

def department_detail(request,pk):
    # return HttpResponse("Hrllo")
    dept = Department.objects.get(id = pk)
    serializer = DepartmentSerializer(dept)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(serializer.data)

def department_list(request):
    # return HttpResponse("Hrllo")
    dept = Department.objects.all()
    serializer = DepartmentSerializer(dept, many = True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def department_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = DepartmentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        else :
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type= 'application/json')

@csrf_exempt       
def department_get(request):
    
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        decoded_data = stream.getvalue().decode('utf-8')
        pythondata = json.dumps(decoded_data)
        # id = pythondata.get('id',None)
        id = pythondata.get('id', None) if isinstance(pythondata, dict) else None

        if id is not None:
            dept = Department.objects.get(id=id)
            serializer = DepartmentSerializer(dept)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type ='application/json')
        dept = Department.objects.all()
        serializer = DepartmentSerializer(dept,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type ='application/json')
    
@csrf_exempt
def department_get_id(request, DepartmentID=None):  # Accept the 'DepartmentID' parameter
    
    if request.method == 'GET':
        if DepartmentID is not None:
            try:
                dept_obj = Department.objects.get(DepartmentID=DepartmentID)  # Assuming 'DepartmentID' is the field name
                serializer = DepartmentSerializer(dept_obj)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except Department.DoesNotExist:
                return HttpResponse(status=404)
        
        dept = Department.objects.all()
        serializer = DepartmentSerializer(dept, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def department_post(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer =DepartmentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'New Department Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json', status = status.HTTP_201_CREATED)
        
        else :
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json')
        
# @csrf_exempt
# def department_put(request):
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         dept_id = pythondata.get('DepartmentID')
#         # dept = Department.objects.filter(DepartmentID=dept_id)
#         # serializer = SiteSerializer(dept,data = pythondata, partial = True) #if partial =False you write then we have give full information fully update
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     res = {'msg':'data updated'}
#         #     json_data = JSONRenderer().render(res)
#         #     return HttpResponse(json_data,content_type = 'application/json')
        
#         # else:
#         #     json_data = JSONRenderer().render(serializer.errors)
#         #     return HttpResponse(json_data,content_type = 'application/json')
#         try:
#             dept = Department.objects.filter(DepartmentID=dept_id)
#             if dept.exists():
#                 # Update the attributes of each site in the queryset
#                 for dept in dept:
#                     serializer = DepartmentSerializer(dept, data=pythondata, partial=True)
#                     if serializer.is_valid():
#                         serializer.save()
#                 response_data = {'msg': 'Data updated'}
#             else:
#                 response_data = {'error': 'No deptartment found with the given DepartmentID'}
#         except :
#             response_data = {'error': 'Department does not exist'}
        
#         return JsonResponse(response_data)

@csrf_exempt
def department_update(request, DepartmentID):
    try:
        dept_obj = Department.objects.get(DepartmentID=DepartmentID)
    except Department.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(dept_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def department_put(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        department_id = pythondata.get('DepartmentID')
        # site = Site.objects.filter(SiteID=site_id)
        # serializer = SiteSerializer(site,data = pythondata, partial = True) #if partial =False you write then we have give full information fully update
        # if serializer.is_valid():
        #     serializer.save()
        #     res = {'msg':'data updated'}
        #     json_data = JSONRenderer().render(res)
        #     return HttpResponse(json_data,content_type = 'application/json')
        
        # else:
        #     json_data = JSONRenderer().render(serializer.errors)
        #     return HttpResponse(json_data,content_type = 'application/json')
        try:
            dept = Department.objects.filter(DepartmentID=department_id)
            if dept.exists():
                # Update the attributes of each site in the queryset
                for dept in dept:
                    serializer = DepartmentSerializer(dept, data=pythondata, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                response_data = {'msg': 'Department updated'}
            else:
                response_data = {'error': 'No department found with the given DepertmentID'}
        except :
            response_data = {'error': 'Department does not exist'}
        
        return JsonResponse(response_data)
    
    

@csrf_exempt
def department_delete(request):       
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        DepartmentID = pythondata.get('DepartmentID')
        # dept = Department.objects.get(DepartmentID=DeprtmentID)
        # dept.delete()
        # res={'msg':'Data Deleted'}
        try:
            dept = Department.objects.get(DepartmentID=DepartmentID)
            dept.delete()
            res = {'msg': f'Department is deleted with the DepartmentID : {DepartmentID}'}
        except :
            res = {'error': 'Departmen not found'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type = 'application/json')
        return JsonResponse(res,safe=False,status = status.HTTP_204_NO_CONTENT)