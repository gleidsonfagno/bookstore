from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializer import ProductSerialize

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerialize(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, intance):
        total = sum([product.price for product in instance.product.all()])
        return total
    
    class Meta:
        model = Product
        fields = ["product", "total"]