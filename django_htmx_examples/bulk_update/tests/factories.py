import datetime
import factory
from django_htmx_examples.bulk_update.models import Customer


class CustomerFactory(factory.Factory):
    class Meta:
        model = Customer

    name = factory.Faker("first_name")
    email = factory.Faker("email")
    status = True
