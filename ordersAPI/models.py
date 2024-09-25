from django.db import models
from customersAPI.models import Customer

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, default='shopping')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for {self.customer.name}"
