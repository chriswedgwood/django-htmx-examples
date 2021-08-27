from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ContactAdmin)
