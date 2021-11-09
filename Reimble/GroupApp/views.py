from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
# Create your views here.


class GroupModelView(APIView):
    def get(self, request):
        query = GroupModel.objects.filter(group_closed=False)
        serializer = GroupModelSerializer(query, many=True)
        return Response(serializer.data)


class GroupPostsView(APIView):
    def get(self, request):
        query = GroupPost.objects.all()
        serializer = GroupPostSerializer(query, many=True)
        return Response(serializer.data)

