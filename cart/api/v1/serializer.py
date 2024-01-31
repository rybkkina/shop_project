from rest_framework import serializers
from shop.models import Product


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
