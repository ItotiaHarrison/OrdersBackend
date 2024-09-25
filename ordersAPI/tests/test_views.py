from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ordersAPI.models import Order
from customersAPI.models import Customer

class OrderViewSetTest(APITestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name='John Doe',
            phone_number='+254700000000',
            email='johndoe@example.com'
        )
        self.order_data = {
            "customer": self.customer.id,
            "product_name": "Product A",
            "amount": 500
        }
        self.order = Order.objects.create(**self.order_data)

    def test_get_orders(self):
        url = reverse('order-list')  # Ensure you have this URL name defined in your URLs
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming there is only one order

    def test_create_order(self):
        url = reverse('order-list')
        response = self.client.post(url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)  # Should now be two orders