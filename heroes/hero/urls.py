from django.urls import path
from heroes.hero.views import HeroList

urlpatterns = [
    path('heroes/', HeroList.as_view()),
]