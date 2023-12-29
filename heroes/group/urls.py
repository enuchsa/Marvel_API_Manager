from django.urls import path
from heroes.group.views import GroupList

urlpatterns = [
    path('groups/', GroupList.as_view()),
]