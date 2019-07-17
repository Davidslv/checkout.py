from bogof_rule import BogofRule
from bulk_discount import BulkDiscount
from item import Item

class Checkout:
    def __init__(self, pricing_rules=[]):
        self.pricing_rules = pricing_rules
        self.basket = []
        self.products = [
            Item(name='Fruit Tea', code='FR1', price=3.11),
            Item(name='Strawberries', code='SR1', price=5.00),
            Item(name='Coffee', code='CF1', price=11.23)
        ]

    def scan(self, product_code):
        for product in self.products:
            if product.code == product_code:
                self.basket.append(product)

    def total(self):
        total = sum(item.price for item in self.basket)

        rule = BogofRule(self.basket)
        total -= rule.discount()

        bulk_rule = BulkDiscount(self.basket)
        total -= bulk_rule.discount()

        return total
