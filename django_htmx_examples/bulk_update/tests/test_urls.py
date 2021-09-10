import pytest
from django.urls import resolve, reverse


def test_bulk_update_customer_status_url():
    assert reverse("bulk-update-customer-status") == f"/bulk-update/"


def test_activate():
    assert reverse("bulk-update-customer-activate") == f"/bulk-update/activate"


def test_deactivate():
    assert reverse("bulk-update-customer-deactivate") == f"/bulk-update/deactivate"
