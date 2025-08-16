from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.settings.models import Library, Book
from apps.settings.serializers import LibrarySerilizer, BookSerializer


class LibraryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        library = Library.objects.all()
        serializer = LibrarySerilizer(library, many=True)
        return Response(serializer.data)    


@method_decorator(cache_page(60), name='dispatch')
class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer