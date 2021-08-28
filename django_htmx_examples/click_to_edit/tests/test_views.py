from django_htmx_examples.test import TestCase
from django_htmx_examples.click_to_edit.tests.factories import ContactFactory
from django_htmx_examples.click_to_edit.models import Contact
from http import HTTPStatus


class TestClickToEdit(TestCase):
    def test_get_status(self):
        response = self.get("")
        self.assert_http_200_ok(response)


class InitialStateTests(TestCase):
    def test_view_with_contact(self):
        contact = Contact.objects.first()  # Mr reinhart is creataed by the migrations
        response = self.client.get("/click-to-edit/")

        assert response.status_code == HTTPStatus.OK
        assert contact.first_name in str(response.content)
        assert contact.last_name in str(response.content)
        assert contact.email_address in str(response.content)


class ContactEditTests(TestCase):
    def test_edit_get(self):
        contact = Contact.objects.first()
        url = f"/contact/{contact.id}/edit/"
        response = self.client.get(url)
        assert response.status_code == HTTPStatus.OK
        assert contact.first_name in str(response.content)
        assert contact.last_name in str(response.content)
        assert contact.email_address in str(response.content)
        assert "Submit" in str(response.content)
        assert "Cancel" in str(response.content)


class ContactUpdateTests(TestCase):
    pass
