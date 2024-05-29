from django.test import TestCase
from order.serializers import OrderSerializer
from order.models import Order
from order.factories import OrderFactory
from product.factories import ProductFactory

class OrderSerializerTest(TestCase):

    def test_order_serializer(self):
        product = ProductFactory()
        order = OrderFactory(product=[product])

        serializer = OrderSerializer(order)

        expected_data = {
            "product": [
                {
                    "title": product.title,
                    "slug": product.slug,
                    "description": product.description,
                    "price": product.price,
                    "active": product.active,
                    "category": [
                        {
                            "title": product.category.title,
                            "slug": product.category.slug,
                            "description": product.category.description,
                            "active": product.category.active,
                        }
                    ]
                }
            ],
            "total": product.price
        }

        self.assertEqual(serializer.data, expected_data)
