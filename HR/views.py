from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import HR
from .serializers import HRSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse   
import io
from rest_framework.parsers import JSONParser,MultiPartParser
from .serializers import HRSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status

# Create your views here.

def hr_detail(request,pk):
    # return HttpResponse("Hrllo")
    hr = HR.objects.get(id = pk)
    serializer = HRSerializer(hr)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(serializer.data)

def hr_list(request):
    # return HttpResponse("Hello")
    hr = HR.objects.all()
    serializer = HRSerializer(hr, many = True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
# @parser_classes([JSONParser, MultiPartParser])
def hr_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = HRSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        else :
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type= 'application/json')
@csrf_exempt       
def hr_get(request): 
    
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        decoded_data = stream.getvalue().decode('utf-8')
        pythondata = json.dumps(decoded_data)
        # id = pythondata.get('id',None)
        id = pythondata.get('id', None) if isinstance(pythondata, dict) else None

        if id is not None:
            site = HR.objects.get(id=id)
            serializer = HRSerializer(site)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type ='application/json')
        site = HR.objects.all()
        serializer = HRSerializer(site,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type ='application/json')

@csrf_exempt
def hr_get_id(request, HRID=None):  # Accept the 'HRID' parameter
    
    if request.method == 'GET':
        if HRID is not None:
            try:
                hr_obj = HR.objects.get(HRID=HRID)  # Assuming 'HRID' is the field name
                serializer = HRSerializer(hr_obj)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except HR.DoesNotExist:
                return HttpResponse(status=404)
        
        site = HR.objects.all()
        serializer = HRSerializer(site, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def hr_post(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer =HRSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json', status = status.HTTP_201_CREATED)
        
        else :
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json')
        
@csrf_exempt
def hr_put(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        hr_id = pythondata.get('HRID')
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
            sites = HR.objects.filter(SiteID=hr_id)
            if sites.exists():
                # Update the attributes of each site in the queryset
                for site in sites:
                    serializer = HRSerializer(site, data=pythondata, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                response_data = {'msg': 'Data updated'}
            else:
                response_data = {'error': 'No sites found with the given HRID'}
        except :
            response_data = {'error': 'HR does not exist'}
        
        return JsonResponse(response_data)
    
from rest_framework.parsers import JSONParser, MultiPartParser

@csrf_exempt
def hr_update(request, HRID):
    try:
        hr_obj = HR.objects.get(HRID=HRID)
    except HR.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        serializer = HRSerializer(hr_obj, data=request.data)  # Use request.data
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def hr_delete(request):       
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        HRID = pythondata.get('HRID')
        # site = Site.objects.get(SiteID=SiteID)
        # site.delete()
        # res={'msg':'Data Deleted'}
        try:
            hr = HR.objects.get(HRID=HRID)
            hr.delete()
            res = {'msg':  f'HR is deleted with the HRID : {HRID}'}
        except :
            res = {'error': 'HR not found'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type = 'application/json')
        return JsonResponse(res,safe=False,status = status.HTTP_204_NO_CONTENT)