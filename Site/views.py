from django.shortcuts import render
from .models import Site
from .serializers import SiteSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse   
import io
from rest_framework.parsers import JSONParser
from .serializers import SiteSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

import json
from rest_framework.views import APIView
from rest_framework import status
from io import BytesIO
from rest_framework.response import Response

# Create your views here.

# def site_detail(request,pk):
#     # return HttpResponse("Hrllo")
#     si = Site.objects.get(id = pk)
#     serializer = SiteSerializer(si)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')
#     # return JsonResponse(serializer.data)


class SiteDetailView(APIView):
    def get(self, request, pk):
        if request.method == 'POST':
            try:
                site = Site.objects.get(id=pk)
                serializer = SiteSerializer(site)
                return Response(serializer.data, status=400)
            except Site.DoesNotExist:
                return Response({"detail": "Site not found."}, status=status.HTTP_404_NOT_FOUND)


def site_list(request):
    si = Site.objects.all()
    serializer = SiteSerializer(si, many = True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

# @csrf_exempt                                        
# def site_create(request):                       
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = SiteSerializer(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
        
#         else :
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data,content_type= 'application/json')


class SiteCreateView(APIView):
    def post(self, request):
        json_data = request.data
        serializer = SiteSerializer(data=json_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt       
# def site_get(request):                 
    
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         # pythondata = JSONParser().parse(stream)
#         decoded_data = stream.getvalue().decode('utf-8')
#         pythondata = json.dumps(decoded_data)
#         # id = pythondata.get('id',None)
#         id = pythondata.get('id', None) if isinstance(pythondata, dict) else None

#         if id is not None:
#             site = Site.objects.get(id=id)
#             serializer = SiteSerializer(site)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type ='application/json')
#         site = Site.objects.all()
#         serializer = SiteSerializer(site,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type ='application/json')


import logging

# ...

class SiteGetView(APIView):
    @csrf_exempt
    def get(self, request):
        try:
            json_data = request.body
            if not json_data:
                return Response("Empty JSON request", status=500)
            
            logging.debug(f"Received JSON data: {json_data}")

            stream = BytesIO(json_data)
            decoded_data = stream.getvalue().decode('utf-8')
            logging.debug(f"Decoded data: {decoded_data}")

            pythondata = json.loads(decoded_data)

            id = pythondata.get('id', None)

            if id is not None:
                site = Site.objects.get(id=id)
                serializer = SiteSerializer(site)
                return Response(serializer.data, content_type='application/json')

            site = Site.objects.all()
            serializer = SiteSerializer(site, many=True)
            return Response(serializer.data, content_type='application/json')
        
        except json.JSONDecodeError as e:
            return Response(f"Invalid JSON format: {str(e)}", status=400)

    
class SiteGetIdView(APIView):
    @csrf_exempt
    def get(self, request, SiteID=None):
        if SiteID is not None:
            try:
                site_obj = Site.objects.get(SiteID=SiteID)  # Assuming 'SiteID' is the field name
                serializer = SiteSerializer(site_obj)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except Site.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        site = Site.objects.all()
        serializer = SiteSerializer(site, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
# @csrf_exempt
# def site_update(request, SiteID):
#     try:
#         site_obj = Site.objects.get(SiteID=SiteID)
#     except Site.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SiteSerializer(site_obj, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

class SiteUpdateView(APIView):
    @csrf_exempt
    def get_object(self, SiteID):
        try:
            return Site.objects.get(SiteID=SiteID)
        except Site.DoesNotExist:
            return None

    def get(self, request, SiteID):
        site_obj = self.get_object(SiteID)
        if site_obj is None:
            return Response(status=500)
        serializer = SiteSerializer(site_obj)
        return JsonResponse(serializer.data)

    def post(self, request, SiteID):
        site_obj = self.get_object(SiteID)
        if site_obj is None:
            return Response(status=400)

        data = JSONParser().parse(request)
        serializer = SiteSerializer(site_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=405)

# @csrf_exempt
# def site_post(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer =SiteSerializer(data = pythondata)
#         try :
#             if serializer.is_valid():
#                 serializer.save()
#                 res = {'msg':'Data Created'}
#                 json_data = JSONRenderer().render(res)
#                 return HttpResponse(json_data,content_type = 'application/json', status = status.HTTP_201_CREATED)
            
#             else :
#                 json_data = JSONRenderer().render(serializer.errors)
#                 return HttpResponse(json_data,content_type = 'application/json')
        
#         except :
#             out = {'error': 'SiteID is already exist please select diffrent SiteID!'}
#             return JsonResponse(out)
        
class SitePostView(APIView):
    @csrf_exempt
    def post(self, request):
        if request.method == 'POST':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            serializer = SiteSerializer(data=pythondata)

            try:
                if serializer.is_valid():
                    serializer.save()
                    res = {'msg': 'Data Created'}
                    json_data = JSONRenderer().render(res)
                    return HttpResponse(json_data, content_type='application/json', status=400)
                else:
                    json_data = JSONRenderer().render(serializer.errors)
                    return HttpResponse(json_data, content_type='application/json')

            except:
                out = {'error': 'SiteID is already exist please select a different SiteID!'}
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

# @csrf_exempt
# def site_delete(request):       
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         SiteID = pythondata.get('SiteID')
#         # site = Site.objects.get(SiteID=SiteID)
#         # site.delete()
#         # res={'msg':'Data Deleted'}
#         try:
#             site = Site.objects.get(SiteID=SiteID)
#             site.delete()
#             res = {'msg': f'Site is deleted with the SiteID : {SiteID}'}
#         except :
#             res = {'error': 'Site not found'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data,content_type = 'application/json')
#         return JsonResponse(res,safe=False,status = status.HTTP_204_NO_CONTENT)


class SiteDeleteView(APIView):
    def delete(self, request):
        data = request.data
        SiteID = data.get('SiteID')

        try:
            site = Site.objects.get(SiteID=SiteID)
            site.delete()
            res = {'msg': f'Site is deleted with the SiteID: {SiteID}'}
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        except Site.DoesNotExist:
            res = {'error': 'Site not found'}
            return JsonResponse(res, safe=False, status=status.HTTP_404_NOT_FOUND)
