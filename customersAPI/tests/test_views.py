from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from customersAPI.models import Customer

class CustomerViewSetTest(APITestCase):

    def setUp(self):
        self.customer_data = {
            "name": "Jane Doe",
            "phone_number": "+254711111111",
            "email": "janedoe@example.com"
        }
        self.customer = Customer.objects.create(**self.customer_data)

    def test_get_customers(self):
        url = reverse('customer-list')  # Ensure you have this URL name defined
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_customer(self):
        url = reverse('customer-list')
        response = self.client.post(url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)  