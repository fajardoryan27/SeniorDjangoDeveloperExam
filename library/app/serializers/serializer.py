from rest_framework import serializers
from ..models import book,Author,Genre


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ('__all__')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')