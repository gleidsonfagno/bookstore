from rest_framework.viewsets import ModelViewSet

from product.models import Product
# from product.serializers.product_serializer import ProductSerializer
from product.serializers.product_serializer import ProductSerialize


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerialize
    
    def get_queryset(self):
        return Product.objects.all()

