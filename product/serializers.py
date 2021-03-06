from rest_framework import serializers
from .models import Product
class ProductSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
                    'name'
        ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
                    'id',
                    'price',
                    'quantity',
                    'name'
            ]