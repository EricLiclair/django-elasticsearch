from rest_framework import serializers
from .models import Product
class ProductSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
                    'name'
        ]