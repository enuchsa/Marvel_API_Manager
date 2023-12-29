from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from heroes.hero.models import Hero
from heroes.hero.serializers import HeroSerializer


class HeroList(APIView):
    def get(self, request, format=None):
        heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)