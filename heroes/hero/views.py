from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from heroes.hero.models import Hero
from heroes.hero.serializers import HeroSerializer


class HeroList(APIView):
    def get(self, request, format=None):
        heroes = Hero.objects.all().filter(group=None)
        serializer = HeroSerializer(heroes, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HeroDetail(APIView):
    def get_object(self, pk):
        try:
            return Hero.objects.get(pk=pk)
        except Hero.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hero = self.get_object(pk)
        serializer = HeroSerializer(hero)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hero = self.get_object(pk)
        serializer = HeroSerializer(hero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hero = self.get_object(pk)
        hero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)