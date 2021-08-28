import datetime
import factory
from django_htmx_examples.click_to_edit.models import Contact


class ContactFactory(factory.Factory):
    class Meta:
        model = Contact

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email_address = factory.Faker("email")
