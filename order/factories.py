import factory

from django.contrib.auth.models import User
from product.factories import ProductFactory

from order.models import Order

class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Facker("pystr")
    username = factory.Facker("pystr")

   

    class Meta:
        model = User

class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, created, extracted, **kwargs):
        if not created:
            return

        if extracted:
            for product in extracted:
                self.product.add(product)
    class Meta:
        model = Order
        
