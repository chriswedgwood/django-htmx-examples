from django_htmx_examples.test import TestCase
from django_htmx_examples.bulk_update.tests.factories import CustomerFactory
from django_htmx_examples.bulk_update.models import Customer
from http import HTTPStatus


class BulkUpdateTests(TestCase):
    def test_get_bulk_update_initial_state(self):
        customer = Customer.objects.first()
        response = self.client.get("/bulk-update/")

        assert response.status_code == HTTPStatus.OK
        assert customer.name in str(response.content)
        assert customer.email in str(response.content)
