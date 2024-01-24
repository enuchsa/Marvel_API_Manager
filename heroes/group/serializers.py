from rest_framework import serializers
from heroes.group.models import Group
from heroes.hero.serializers import HeroSerializer


class GroupSerializer(serializers.ModelSerializer):
    heroes = HeroSerializer(many=True, allow_null=True, required=False)
    
    class Meta:
        model = Group
        fields = ['id','name', 'description', 'heroes']
        