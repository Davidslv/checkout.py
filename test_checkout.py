import unittest
from checkout import Checkout

class TestCheckout(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.checkout = Checkout()

    def test_without_discount(self):
        self.checkout.scan('FR1')
        self.assertEqual(self.checkout.total(), 3.11)

    def test_buy_one_get_one_free_fruit_tea(self):
        self.checkout.scan('FR1')
        self.checkout.scan('FR1')
        self.assertEqual(self.checkout.total(), 3.11)

    def test_buy_one_get_one_free_discount(self):
        self.checkout.scan('FR1')
        self.checkout.scan('SR1')
        self.checkout.scan('FR1')
        self.checkout.scan('FR1')
        self.checkout.scan('CF1')

        self.assertEqual(self.checkout.total(), 22.45)

    def test_bulk_discount(self):
        self.checkout.scan('SR1')
        self.checkout.scan('SR1')
        self.checkout.scan('FR1')
        self.checkout.scan('SR1')

        self.assertEqual(self.checkout.total(), 16.61)
