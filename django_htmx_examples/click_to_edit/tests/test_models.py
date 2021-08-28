import datetime
import pytest
from django.utils import timezone
from django_htmx_examples.test import TestCase
from django_htmx_examples.click_to_edit.models import Contact
from django_htmx_examples.click_to_edit.tests.factories import ContactFactory


class TestContact(TestCase):
    def test_str(self):
        contact = ContactFactory()

        assert str(contact) == f"{contact.first_name} {contact.last_name}"  # pytest

    def test_factory(self):
        contact = ContactFactory()

        assert contact is not None
        assert contact.email_address != ""
