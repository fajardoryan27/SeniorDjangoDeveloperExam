from rest_framework import serializers
from ..app.models import book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ('__all__')
