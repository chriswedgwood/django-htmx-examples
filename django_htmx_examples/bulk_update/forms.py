from django import forms


from .models import Customer


class CustomerStatusForm(forms.ModelForm):
    checkbox = forms.CheckboxInput()

    class Meta:
        model = Customer
        fields = ("name", "email", "status")
