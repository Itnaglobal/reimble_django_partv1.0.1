from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
# Create your views here.


class CountryApiView(APIView):
    def get(self, request):
        data = []
        query = Country.objects.all()
        serializers = CountrySerializers(query, many=True)
        return Response(serializers.data)


class ProfessionsApiView(APIView):
    def get(self, request):
        data = []
        query = Professions.objects.all()
        serializers = ProfessionSerializer(query, many=True)
        return Response(serializers.data)


class UserSerializerApiview(APIView):
    def get(self, request):
        data = []
        query = UserModel.objects.all()
        user_serilizer = UserSerializer(query, many=True)
        return Response(user_serilizer.data)
