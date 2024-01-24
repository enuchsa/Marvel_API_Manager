from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from heroes.auth.serializers import UserSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class UserView(APIView):
    
    def get(self, request):
        username = request.query_params.get('username')
        user = User.objects.get(username=username)
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(username=username, password=password)
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    
    