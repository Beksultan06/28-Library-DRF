from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, \
RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.mixins import ListModelMixin, CreateModelMixin, \
RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.settings.models import Library, Book
from apps.settings.serializers import LibrarySerilizer, BookSerializer,\
 BookDetailSerializer

@method_decorator(cache_page(60), name='dispatch')
class BookAPIList(GenericViewSet, ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPI(GenericViewSet, 
              CreateModelMixin,
              RetrieveModelMixin,
              UpdateModelMixin,
              DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

# class LibraryAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         library = Library.objects.all()
#         serializer = LibrarySerilizer(library, many=True)
#         return Response(serializer.data)    
# 
# 
# @method_decorator(cache_page(60), name='dispatch')
# class BookAPIView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
# 
# 
# class BookCreateAPIView(CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
# 
# 
# class BookRetrieveAPIVIEW(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookDetailSerializer
# 
# 
# class BookUdateAPIView(UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
# 
# class BookDeleteAPIView(DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer