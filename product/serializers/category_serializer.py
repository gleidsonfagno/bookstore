from rest_framework import serializers

from product.models.category  import Category

class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "title",
            "slug",
            "description",
            "active",
        ]