from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from heroes.hero.models import Hero
from heroes.hero.serializers import HeroSerializer
from heroes.api import Marvel_api

class HeroList(APIView):
    heroes = []

    def get(self, request):
        self.heroes = Marvel_api().get_all()
        
        serializer = HeroSerializer(self.heroes, many=True)
        return Response(serializer.data)
    
    def get(self, request, *args, **kwargs):
        params = request.query_params
        
        self.heroes = Marvel_api().get_all(params)
        heroes_in_group = [hero.id for hero in Hero.objects.all()]
        
        if params.get('status') == 'EM GRUPO':
            herois_final = [hero for hero in self.heroes if hero.id in heroes_in_group]
        elif params.get('status') == 'SEM GRUPO':
            herois_final = [hero for hero in self.heroes if hero.id not in heroes_in_group]
        else:
            herois_final = self.heroes    
        
        
        serializer = HeroSerializer(herois_final, many=True)
        return Response(serializer.data)
        
    
class HeroDetail(APIView):

    def get(self, request, pk, format=None):
        hero = Marvel_api().get_one(pk)[0]
        serializer = HeroSerializer(hero)
        return Response(serializer.data)


    