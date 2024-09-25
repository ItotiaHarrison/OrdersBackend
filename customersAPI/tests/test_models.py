from django.test import TestCase
from customersAPI.models import Customer

class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name='John Doe',
            phone_number='+254700000000',
            email='johndoe@example.com'
        )

    def test_customer_creation(self):
        self.assertIsInstance(self.customer, Customer)
        self.assertEqual(self.customer.name, 'John Doe')
        self.assertEqual(self.customer.phone_number, '+254700000000')

    def test_customer_string_representation(self):
        self.assertEqual(str(self.customer), self.customer.name)