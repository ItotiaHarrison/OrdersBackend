from django.test import TestCase
from ordersAPI.models import Order
from customersAPI.models import Customer

class OrderModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name='John Doe',
            phone_number='+254700000000',
            email='johndoe@example.com'
        )
        self.order = Order.objects.create(
            customer=self.customer,
            product_name='Product A',
            amount=500
        )

    def test_order_creation(self):
        self.assertIsInstance(self.order, Order)
        self.assertEqual(self.order.product_name, 'Product A')
        self.assertEqual(self.order.customer.name, 'John Doe')

    def test_order_string_representation(self):
        self.assertEqual(str(self.order), f"Order {self.order.id}")