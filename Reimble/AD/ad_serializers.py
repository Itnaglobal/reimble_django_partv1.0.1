from rest_framework import serializers
from .models import *


class ADSerializer(serializers.ModelSerializer):
    class Meta:
        model = AD
        fields = '__all__'
