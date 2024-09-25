from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, default='+254700000000')
    email = models.EmailField(unique=True, default='default@example.com')

    def __str__(self):
        return self.name