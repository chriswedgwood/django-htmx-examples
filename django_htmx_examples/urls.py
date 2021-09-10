"""django_htmx_examples URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
import django_htmx_examples.click_to_edit.views as click_to_edit_views
import django_htmx_examples.bulk_update.views as bulk_update_views


urlpatterns = [
    path("", TemplateView.as_view(template_name="examples.html"), name="examples-list"),
    path("admin/", admin.site.urls),
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
    path(
        "bulk-update/",
        bulk_update_views.customer_status,
        name="bulk-update-customer-status",
    ),
    path(
        "bulk-update/activate",
        bulk_update_views.customer_activate,
        name="bulk-update-customer-activate",
    ),
    path(
        "bulk-update/deactivate",
        bulk_update_views.customer_deactivate,
        name="bulk-update-customer-deactivate",
    ),
]
