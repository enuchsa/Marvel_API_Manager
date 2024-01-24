from django.urls import path, include


urlpatterns = [
    path('', include('heroes.auth.urls')),
    path('', include('heroes.group.urls')),
    path('', include('heroes.hero.urls')),
]
    
