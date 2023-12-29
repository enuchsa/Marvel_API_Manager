from rest_framework import serializers
from heroes.group.models import Group


class GroupSerializer(serializers.ModelSerializer):
    heroes = serializers.StringRelatedField(many=True, allow_null=True, required=False)
    
    class Meta:
        model = Group
        fields = ['name', 'description', 'heroes']