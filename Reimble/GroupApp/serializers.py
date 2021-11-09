from rest_framework import serializers
from .models import *


class GroupModelSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = GroupModel
        fields = ['group_name', 'group_profile_picture', 'user', 'group_closed', 'groups']


class GroupPostSerializer(serializers.ModelSerializer):
    # group = serializers.StringRelatedField(many=True)

    class Meta:
        model = GroupPost
        fields = ['group', 'title', 'content', 'attachments']
