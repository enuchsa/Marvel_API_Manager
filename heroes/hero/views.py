from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from heroes.hero.models import Hero
from heroes.hero.serializers import HeroSerializer


class HeroList(APIView):
    URL = "http://gateway.marvel.com/v1/public/characters"
    heroes = []

    def get(self, request, format=None):
        response = requests.get(
            self.URL,
            params={
                "ts": "100",
                "apikey": "16e90537a937e7b409088e3f860ebab2",
                "hash": "107b7a9b68745b0157bb5e2def3130d8",
                "offset": 0,
                "limit": 100,
            },
            verify=False
        )

        heroes_list = response.json()
        for hero in heroes_list['data']['results']:
            hero_model = Hero()
            hero_model.id = hero['id']
            hero_model.name = hero['name']
            hero_model.description = hero['description']
            hero_model.image = hero['thumbnail']['path'] + '.' + hero['thumbnail']['extension']
            self.heroes.append(hero_model)
            
        
        serializer = HeroSerializer(self.heroes, many=True)
        return Response(serializer.data)
        
    
    
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
    
def fetch():
    URL = "http://gateway.marvel.com/v1/public/characters"

    def get(self, request, format=None):
        response = requests.get(
            self.URL,
            params={
                "ts": "100",
                "apikey": "16e90537a937e7b409088e3f860ebab2",
                "hash": "107b7a9b68745b0157bb5e2def3130d8",
                "offset": 0,
                "limit": 100,
            },
            verify=False
        )

        heroes_list = response.json()

        return heroes_list