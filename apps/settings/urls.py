from django.urls import path
from apps.settings.views import LibraryAPIView

urlpatterns = [
    path("list-library", LibraryAPIView.as_view(), name='list-library')
]