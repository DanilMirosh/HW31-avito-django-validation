from pytest_factoryboy import register
from test.factories import AdFactory, CategoryFactory, UserFactory

pytest_plugins = "tests.fixtures"

register(AdFactory)
register(CategoryFactory)
register(UserFactory)
