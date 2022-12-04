import factory.django

from ads.models import Ad
from .user import UserFactory
from .category import CategoryFactory


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "Test 10 characters minimum"
    price = 1000

    is_published = False
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
