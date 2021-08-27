from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=50)
    last_name = models.CharField(null=False, blank=False, max_length=50)
    email_address = models.EmailField(null=False, blank=False, max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
