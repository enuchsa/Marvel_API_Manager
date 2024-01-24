from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from heroes.hero.views import HeroList, HeroDetail

urlpatterns = [
    path('herois/', HeroList.as_view(), ),
    path('herois/<int:pk>/', HeroDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)