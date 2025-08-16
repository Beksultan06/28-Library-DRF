from django.urls import path
from apps.settings.views import LibraryAPIView, BookAPIView

urlpatterns = [
    path("list-library", LibraryAPIView.as_view(), name='list-library'),
    path("book-list", BookAPIView.as_view(), name='book-list')
]