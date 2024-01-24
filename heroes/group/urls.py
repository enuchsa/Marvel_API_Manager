from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from heroes.group.views import GroupList, GroupDetail

urlpatterns = [
    path('grupos/', GroupList.as_view()),
    path('grupos/<int:pk>/', GroupDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)