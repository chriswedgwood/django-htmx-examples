from django import forms
from django.utils.text import slugify

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "border border-red-900 text-lg w-1/2 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-yellow-200 rounded-md"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "max-w-lg block w-full shadow-sm focus:ring-red-500 border-yellow-200 focus:border-red-500 sm:max-w-xs sm:text-lg border-gray-300 rounded-md"
                }
            ),
            "email_address": forms.TextInput(
                attrs={
                    "class": "max-w-lg block w-full shadow-sm focus:ring-red-500 border-yellow-200 focus:border-red-500 sm:max-w-xs sm:text-lg border-gray-300 rounded-md"
                }
            ),
        }
        fields = ("first_name", "last_name", "email_address")
