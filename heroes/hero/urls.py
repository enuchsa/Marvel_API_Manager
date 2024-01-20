from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from heroes.hero.views import HeroList, HeroDetail

urlpatterns = [
    path('heroes/', HeroList.as_view()),
    # path('heroes/<str:name>', HeroList.as_view()),
    path('hero/<int:pk>/', HeroDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)