import unittest
from checkout import Checkout
from bogof_rule import BogofRule
from bulk_discount import BulkDiscount

class TestCheckout(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.checkout = Checkout(pricing_rules=[BogofRule, BulkDiscount])

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
