import factory

from product.models import Product
from product.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Facker("pystr")
    slug = factory.Facker("pystr")
    description = factory.Facker("pystr")
    active = factory.Interator([True, False])

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Facker("pystr")
    category = factory.LazyAttribute(category)
    active = factory.Facker("pystr")

    @factory.post_generation
    def category(self, created, extracted, **kwargs):
        if not created:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)
    class Meta:
        model = Product
