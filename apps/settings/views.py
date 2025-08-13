from rest_framework.views import APIView
from rest_framework.response import Response

from apps.settings.models import Library
from apps.settings.serializers import LibrarySerilizer


class LibraryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        library = Library.objects.all()
        serializer = LibrarySerilizer(library, many=True)
        return Response(serializer.data)    