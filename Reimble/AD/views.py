from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .ad_serializers import *

class AdView(APIView):
    def get(self, request):
        data = []
        ad_query = AD.objects.all()
        ad_serializer = ADSerializer(ad_query, many=True)
        return Response(ad_serializer.data)
