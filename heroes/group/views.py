from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection


from heroes.group.models import Group
from heroes.hero.models import Hero
from heroes.group.serializers import GroupSerializer
from heroes.hero.serializers import HeroSerializer
from heroes.api import Marvel_api


class GroupList(APIView):
    

    # def execute_raw_query(self, hero: Hero, group_id: int):    
    #     breakpoint()
    #     with connection.cursor() as cursor:
    #         cursor.execute(f"""
    #             INSERT INTO heroes_hero (name, description, image, group_id, id) VALUES ({hero.name, hero.description, hero.image, group_id, hero.id}); 
    #         """)
    #         results = cursor.fetchall()
    #         return results
    
    def get(self, request, format=None):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        pks = data['heroes']
        data['heroes'] = []
        print(pks)
        group = Group(name=data['name'], description=data['description'])
        group.save()
        
        hero: Hero
        for pk in pks:
            hero = Marvel_api().get_one(pk)[0]
            hero.group = group
            hero.save()   
            
            # response = self.execute_raw_query(hero[0], group.id)
        serializer = GroupSerializer(data=data)
        
        
        if serializer.is_valid():
            # serializer.save()
            group = Group.objects.get(pk=group.pk)
            serializer = GroupSerializer(group)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GroupDetail(APIView):
    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        data = request.data
        print(data)
        group = Group.objects.get(pk=pk)
        pk_g = group.pk
        
        for pk in data['heroes']:
            hero = Marvel_api().get_one(pk)[0]
            hero.group = group
            hero.save()
            
        lis = {}
        lis['name'] = group.name
        lis['description'] = group.description
        lis['heroes'] = []
        serializer = GroupSerializer(data=lis)
        if serializer.is_valid():
            group = Group.objects.get(pk=pk_g)
            serializer = GroupSerializer(group)
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        group = self.get_object(pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)