from rest_framework import serializers

from apps.settings.models import Library

class LibrarySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'title', 'description', 'image']