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
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# def hr_detail(request,pk):
#     # return HttpResponse("Hrllo")
#     hr = HR.objects.get(HRID = pk)
#     serializer = HRSerializer(hr)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')
#     # return JsonResponse(serializer.data)

class HRDetailView(APIView):
    def get(self, request, pk):
        try:
            hr = HR.objects.get(HRID=pk)
        except HR.DoesNotExist:
            return HttpResponse("HR not found", status=404)

        serializer = HRSerializer(hr)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

# def hr_list(request):
#     # return HttpResponse("Hello")
#     hr = HR.objects.all()
#     serializer = HRSerializer(hr, many = True)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data,content_type='application/json')
#     return JsonResponse(serializer.data,safe=False)

class HRListView(APIView):
    def get(self, request):
        hr = HR.objects.all()
        serializer = HRSerializer(hr, many=True)
        return JsonResponse(serializer.data, safe=False)


# @csrf_exempt
# # @parser_classes([JSONParser, MultiPartParser])
# def hr_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = HRSerializer(data = pythondata)
#         if serializer.is_valHRID():
#             serializer.save()
#             res={'msg':'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
        
#         else :
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data,content_type= 'application/json')


#@csrf_exempt
#@parser_classes([JSONParser, MultiPartParser])
class HRCreateView(APIView):
    def post(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = HRSerializer(data=pythondata)
        if serializer.is_valHRID():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')


# @csrf_exempt     
# def hr_get(request): 
    
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         # pythondata = JSONParser().parse(stream)
#         decoded_data = stream.getvalue().decode('utf-8')
#         pythondata = json.dumps(decoded_data)
#         # HRID = pythondata.get('HRID',None)
#         HRID = pythondata.get('HRID', None) if isinstance(pythondata, dict) else None

#         if HRID is not None:
#             site = HR.objects.get(HRID=HRID)
#             serializer = HRSerializer(site)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type ='application/json')
#         site = HR.objects.all()
#         serializer = HRSerializer(site,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type ='application/json')

#@csrf_exempt
#@parser_classes([JSONParser])
class HRGetView(APIView):
    def get(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        decoded_data = stream.getvalue().decode('utf-8')
        pythondata = json.loads(decoded_data)
        HRID = pythondata.get('HRID', None)

        if HRID is not None:
            try:
                site = HR.objects.get(HRID=HRID)
                serializer = HRSerializer(site)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except HR.DoesNotExist:
                return Response({"error": "HR object with this HRID does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        sites = HR.objects.all()
        serializer = HRSerializer(sites, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
# @csrf_exempt
# def hr_get_HRID(request, HRHRID=None):  # Accept the 'HRHRID' parameter
    
#     if request.method == 'GET':
#         if HRHRID is not None:
#             try:
#                 hr_obj = HR.objects.get(HRHRID=HRHRID)  # Assuming 'HRHRID' is the field name
#                 serializer = HRSerializer(hr_obj)
#                 json_data = JSONRenderer().render(serializer.data)
#                 return HttpResponse(json_data, content_type='application/json')
#             except HR.DoesNotExist:
#                 return HttpResponse(status=404)
        
#         site = HR.objects.all()
#         serializer = HRSerializer(site, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')

#@csrf_exempt
#@parser_classes([JSONParser])
class HRGetView(APIView):
    def get(self, request, HRID=None):
        if HRID is not None:
            try:
                hr_obj = HR.objects.get(HRID=HRID)  # Assuming 'HRHRID' is the field name
                serializer = HRSerializer(hr_obj)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except HR.DoesNotExist:
                return Response({"error": "HR object with this HRHRID does not exist"}, status=status.HTTP_404_NOT_FOUND)

        sites = HR.objects.all()
        serializer = HRSerializer(sites, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

# @csrf_exempt
# def hr_post(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer =HRSerializer(data = pythondata)
#         if serializer.is_valHRID():
#             serializer.save()
#             res = {'msg':'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type = 'application/json', status = status.HTTP_201_CREATED)
        
#         else :
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data,content_type = 'application/json')

class HRPostView(APIView):
    def post(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = HRSerializer(data=pythondata)
        if serializer.is_valHRID():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json', status=status.HTTP_201_CREATED)
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

# @csrf_exempt
# def hr_put(request):
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         hr_HRID = pythondata.get('HRHRID')
#         # site = Site.objects.filter(SiteHRID=site_HRID)
#         # serializer = SiteSerializer(site,data = pythondata, partial = True) #if partial =False you write then we have give full information fully update
#         # if serializer.is_valHRID():
#         #     serializer.save()
#         #     res = {'msg':'data updated'}
#         #     json_data = JSONRenderer().render(res)
#         #     return HttpResponse(json_data,content_type = 'application/json')
        
#         # else:
#         #     json_data = JSONRenderer().render(serializer.errors)
#         #     return HttpResponse(json_data,content_type = 'application/json')
#         try:
#             sites = HR.objects.filter(SiteHRID=hr_HRID)
#             if sites.exists():
#                 # Update the attributes of each site in the queryset
#                 for site in sites:
#                     serializer = HRSerializer(site, data=pythondata, partial=True)
#                     if serializer.is_valHRID():
#                         serializer.save()
#                 response_data = {'msg': 'Data updated'}
#             else:
#                 response_data = {'error': 'No sites found with the given HRHRID'}
#         except :
#             response_data = {'error': 'HR does not exist'}
        
#         return JsonResponse(response_data)
    
# from rest_framework.parsers import JSONParser, MultiPartParser

# @csrf_exempt
# def hr_update(request, HRHRID):
#     try:
#         hr_obj = HR.objects.get(HRHRID=HRHRID)
#     except HR.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'POST':
#         serializer = HRSerializer(hr_obj, data=request.data)  # Use request.data
#         if serializer.is_valHRID():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def hr_delete(request):       
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         HRHRID = pythondata.get('HRHRID')
#         # site = Site.objects.get(SiteHRID=SiteHRID)
#         # site.delete()
#         # res={'msg':'Data Deleted'}
#         try:
#             hr = HR.objects.get(HRHRID=HRHRID)
#             hr.delete()
#             res = {'msg':  f'HR is deleted with the HRHRID : {HRHRID}'}
#         except :
#             res = {'error': 'HR not found'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data,content_type = 'application/json')
#         return JsonResponse(res,safe=False,status = status.HTTP_204_NO_CONTENT)
    

class HRPutView(APIView):
    def put(self, request):
        json_data = request.body
        pythondata = JSONParser().parse(json_data)
        hr_HRID = pythondata.get('HRHRID')

        try:
            sites = HR.objects.filter(HRHRID=hr_HRID)
            if sites.exists():
                # Update the attributes of each HR in the queryset
                for site in sites:
                    serializer = HRSerializer(site, data=pythondata, partial=True)
                    if serializer.is_valHRID():
                        serializer.save()
                response_data = {'msg': 'Data updated'}
            else:
                response_data = {'error': 'No HR found with the given HRHRID'}
        except HR.DoesNotExist:
            response_data = {'error': 'HR does not exist'}
        
        return JsonResponse(response_data)
    
from rest_framework.parsers import JSONParser, MultiPartParser

#@csrf_exempt
class HRUpdateView(APIView):
    def get_object(self, HRHRID):
        try:
            return HR.objects.get(HRHRID=HRHRID)
        except HR.DoesNotExist:
            return None

    def post(self, request, HRHRID):
        hr_obj = self.get_object(HRHRID)
        if hr_obj is None:
            return HttpResponse(status=404)

        serializer = HRSerializer(hr_obj, data=request.data)
        if serializer.is_valHRID():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


#@csrf_exempt
#@parser_classes([JSONParser])
class HRDeleteView(APIView):
    def delete(self, request):
        json_data = request.body
        pythondata = JSONParser().parse(json_data)
        HRHRID = pythondata.get('HRHRID')
        
        try:
            hr = HR.objects.get(HRHRID=HRHRID)
            hr.delete()
            response_data = {'msg': f'HR is deleted with the HRHRID: {HRHRID}'}
        except HR.DoesNotExist:
            response_data = {'error': 'HR not found'}

        return JsonResponse(response_data, safe=False, status=status.HTTP_204_NO_CONTENT)
