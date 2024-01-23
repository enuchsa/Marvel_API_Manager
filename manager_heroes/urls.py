from django.urls import path, include


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include('heroes.group.urls')),
    path('', include('heroes.hero.urls')),
]
    
