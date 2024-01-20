from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from heroes.hero.models import Hero
from heroes.hero.serializers import HeroSerializer
from heroes.api import Marvel_api

class HeroList(APIView):
    URL = "http://gateway.marvel.com/v1/public/characters"
    heroes = []

    def get(self, request, format=None):
        self.heroes = Marvel_api().get_all()
        # response = requests.get(
        #     self.URL,
        #     params={
        #         # "name": name,
        #         "ts": "100",
        #         "apikey": "16e90537a937e7b409088e3f860ebab2",
        #         "hash": "107b7a9b68745b0157bb5e2def3130d8",
        #         "offset": 0,
        #         "limit": 100,
        #     },
        #     verify=False
        # )

        # heroes_list = response.json()
        # print(heroes_list)
        # for hero in heroes_list['data']['results']:
        #     hero_model = Hero()
        #     hero_model.id = hero['id']
        #     hero_model.name = hero['name']
        #     hero_model.description = hero['description']
        #     hero_model.image = hero['thumbnail']['path'] + '.' + hero['thumbnail']['extension']
        #     self.heroes.append(hero_model)
            
        
        serializer = HeroSerializer(self.heroes, many=True)
        return Response(serializer.data)
        
    
    
class HeroDetail(APIView):
    URL = "http://gateway.marvel.com/v1/public/characters"

    def get(self, request, pk, format=None):
        response = requests.get(
            self.URL + f'/{pk}',
            params={
                "ts": "100",
                "apikey": "16e90537a937e7b409088e3f860ebab2",
                "hash": "107b7a9b68745b0157bb5e2def3130d8",
                "offset": 0,
                "limit": 100,
            },
            verify=False
        )
        
        hero = response.json()
        hero = hero['data']['results']
        
        hero_model = Hero()
        hero_model.id = hero[0]['id']
        hero_model.name = hero[0]['name']
        hero_model.description = hero[0]['description']
        hero_model.image = hero[0]['thumbnail']['path'] + '.' + hero[0]['thumbnail']['extension']
        
        serializer = HeroSerializer(hero_model)
        return Response(serializer.data)


    