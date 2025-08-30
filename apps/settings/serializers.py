from rest_framework import serializers

from apps.settings.models import Library, Book, Author, Reader, Borrowing

class LibrarySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'title', 'description', 'image']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", 'title', 'desscription', 'author']

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", 'title', 'desscription', 'price', 'author']

class ReaderSerializer(serializers.ModelSerializer):
    reader = serializers.PrimaryKeyRelatedField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Borrowing
        fields = ['id', 'reader', 'book', 'borrowed_at', 'return_date', 'returned']

    def create(self, validated_data):
        user = self.context['request'].user
        reader = Reader.objects.get(user=user)
        validated_data['reader'] = reader

        book - validated_data['book']
        if book.available_copies <= 0:
            raise serializers.ValidationError("Нет книг")

        borrowing = Borrowing.objects.create(**validated_data)
        return borrowing