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


class SiteCreateView(APIView):
    def post(self, request):
        json_data = request.data
        serializer = SiteSerializer(data=json_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


import logging


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