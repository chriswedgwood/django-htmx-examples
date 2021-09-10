import datetime
import pytest
from django.utils import timezone
from django_htmx_examples.test import TestCase
from django_htmx_examples.bulk_update.models import Customer
from django_htmx_examples.bulk_update.tests.factories import CustomerFactory


class TestCustomer(TestCase):
    def test_str(self):
        customer = CustomerFactory()

        assert str(customer) == f"{customer.name}"  # pytest

    def test_factory(self):
        customer = CustomerFactory()

        assert customer is not None
        assert customer.email != ""
