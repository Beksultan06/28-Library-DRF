from rest_framework import serializers

from apps.settings.models import Library, Book, Author

class LibrarySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'title', 'description', 'image']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", 'title', 'desscription', 'author']