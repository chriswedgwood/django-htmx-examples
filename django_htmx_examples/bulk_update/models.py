from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    email = models.EmailField(null=False, blank=False, max_length=254)
    status = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return f"{self.name}"
