from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializer import CategorySerializer

class ProductSerialize(serializers.ModelSerializer):
    category = CategorySerializer(require=True, many=True)

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "active",
            "category",
        ]