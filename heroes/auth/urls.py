from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from heroes.auth.views import UserView

urlpatterns = [
    path('auth/register/', UserView.as_view(), name='create_user'),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]