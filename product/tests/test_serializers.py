from django.test import TestCase
from product.serializers import ProductSerializer, CategorySerializer
from product.models import Product, Category
from product.factories import ProductFactory, CategoryFactory

# Test for CategorySerializer
class CategorySerializerTest(TestCase):

    def test_category_serializer(self):
        category = CategoryFactory()

        # Serializes the category instance
        serializer = CategorySerializer(category)

        expected_data = {
            "title": category.title,
            "slug": category.slug,
            "description": category.description,
            "active": category.active,
        }

        # Compares the serialized data with the expected data
        self.assertEqual(serializer.data, expected_data)

# Test for ProductSerializer
class ProductSerializerTest(TestCase):

    def test_product_serializer(self):
        category = CategoryFactory()
        product = ProductFactory(category=[category])

        # Serializes the product instance
        serializer = ProductSerializer(product)

        expected_data = {
            "title": product.title,
            "description": product.description,
            "price": product.price,
            "active": product.active,
            "category": [
                {
                    "title": category.title,
                    "slug": category.slug,
                    "description": category.description,
                    "active": category.active,
                }
            ]
        }

        # Compares the serialized data with the expected data
        self.assertEqual(serializer.data, expected_data)
