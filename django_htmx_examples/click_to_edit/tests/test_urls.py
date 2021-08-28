import pytest
from django.urls import resolve, reverse


def test_root():
    assert reverse("examples-list") == f"/"


def test_initial_state():
    assert reverse("click-to-edit-initial-state") == f"/click-to-edit/"


def test_contact_edit():
    assert reverse("contact-edit", args=[1]) == f"/contact/1/edit/"


def test_contact_update():
    assert reverse("contact-update", args=[1]) == f"/contact/1/"


"""
 path(
        "click-to-edit/",
        click_to_edit_views.initial_state,
        name="click-to-edit-initial-state",
    ),
    path(
        "contact/<int:contact_id>/edit/",
        click_to_edit_views.contact_edit,
        name="contact-edit",
    ),
    path(
        "contact/<int:contact_id>/",
        click_to_edit_views.contact_detail,
        name="contact-update",
    ),
]
"""
