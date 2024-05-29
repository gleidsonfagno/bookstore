import factory

from product.models import Product
from product.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Interator([True, False])

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pystr")
    category = factory.LazyAttribute(category)
    active = factory.Faker("pystr")

    @factory.post_generation
    def category(self, created, extracted, **kwargs):
        if not created:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)
    class Meta:
        model = Product
