from django.shortcuts import render
from .models import Site
from .serializers import SiteSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse   
import io
from rest_framework.parsers import JSONParser
from .serializers import SiteSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status

# Create your views here.

def site_detail(request,pk):
    # return HttpResponse("Hrllo")
    si = Site.objects.get(id = pk)
    serializer = SiteSerializer(si)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(serializer.data)

def site_list(request):
    # return HttpResponse("Hrllo")
    si = Site.objects.all()
    serializer = SiteSerializer(si, many = True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def site_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = SiteSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        else :
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type= 'application/json')

@csrf_exempt       
def site_get(request): 
    
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        decoded_data = stream.getvalue().decode('utf-8')
        pythondata = json.dumps(decoded_data)
        # id = pythondata.get('id',None)
        id = pythondata.get('id', None) if isinstance(pythondata, dict) else None

        if id is not None:
            site = Site.objects.get(id=id)
            serializer = SiteSerializer(site)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type ='application/json')
        site = Site.objects.all()
        serializer = SiteSerializer(site,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type ='application/json')
    
@csrf_exempt
def site_get_id(request, SiteID=None):  # Accept the 'SiteID' parameter
    
    if request.method == 'GET':
        if SiteID is not None:
            try:
                site_obj = Site.objects.get(SiteID=SiteID)  # Assuming 'SiteID' is the field name
                serializer = SiteSerializer(site_obj)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except Site.DoesNotExist:
                return HttpResponse(status=404)
        
        site = Site.objects.all()
        serializer = SiteSerializer(site, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
 
@csrf_exempt
def site_update(request, SiteID):
    try:
        site_obj = Site.objects.get(SiteID=SiteID)
    except Site.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SiteSerializer(site_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def site_post(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer =SiteSerializer(data = pythondata)
        try :
            if serializer.is_valid():
                serializer.save()
                res = {'msg':'Data Created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data,content_type = 'application/json', status = status.HTTP_201_CREATED)
            
            else :
                json_data = JSONRenderer().render(serializer.errors)
                return HttpResponse(json_data,content_type = 'application/json')
        
        except :
            out = {'error': 'SiteID is already exist please select diffrent SiteID!'}
            return JsonResponse(out)
        
# @csrf_exempt
# def site_put(request):
#      if request.method == 'POST':
#         try:
#             json_data = request.body
#             print("ok")

#             pythondata = JSONParser().parse(json_data)
#             # print("ok")

#             # Validate the data using the serializer
#             serializer = SiteSerializer(data=pythondata, partial=True)
#             if serializer.is_valid():
#                 site_id = pythondata.get('SiteID')
#                 sites = Site.objects.filter(SiteID=site_id)

#                 if sites.exists():
#                     for site in sites:
#                         serializer.update(site, pythondata)  # Update the site using the serializer
#                     response_data = {'msg': 'Data updated'}
#                 else:
#                     response_data = {'error': 'No sites found with the given SiteID'}
#             else:
#                 response_data = {'error': 'Validation failed', 'errors': serializer.errors}
#         except Exception as e:
#             print("ok")

#             response_data = {'error': str(e)}
        
#         return JsonResponse(response_data)
    # if request.method == 'POST':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     site_id = pythondata.get('SiteID')
    #     # site = Site.objects.filter(SiteID=site_id)
    #     # serializer = SiteSerializer(site,data = pythondata, partial = True) #if partial =False you write then we have give full information fully update
    #     # if serializer.is_valid():
    #     #     serializer.save()
    #     #     res = {'msg':'data updated'}
    #     #     json_data = JSONRenderer().render(res)
    #     #     return HttpResponse(json_data,content_type = 'application/json')
        
    #     # else:
    #     #     json_data = JSONRenderer().render(serializer.errors)
    #     #     return HttpResponse(json_data,content_type = 'application/json')
    #     try:
    #         sites = Site.objects.filter(SiteID=site_id)
    #         if sites.exists():
    #             # Update the attributes of each site in the queryset
    #             for site in sites:
                    
    #                 serializer = SiteSerializer(site, data=pythondata, partial=True)
    #                 print("ok")
    #                 if serializer.is_valid():
    #                     serializer.save()
                        
    #             response_data = {'msg': 'Data updated'}
    #         else:
    #             response_data = {'error': 'No sites found with the given SiteID'}
    #     except :
    #         response_data = {'error': 'Site does not exist'}
        
    #     return JsonResponse(response_data)

@csrf_exempt
def site_delete(request):       
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        SiteID = pythondata.get('SiteID')
        # site = Site.objects.get(SiteID=SiteID)
        # site.delete()
        # res={'msg':'Data Deleted'}
        try:
            site = Site.objects.get(SiteID=SiteID)
            site.delete()
            res = {'msg': f'Site is deleted with the SiteID : {SiteID}'}
        except :
            res = {'error': 'Site not found'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type = 'application/json')
        return JsonResponse(res,safe=False,status = status.HTTP_204_NO_CONTENT)