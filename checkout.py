from bogof_rule import BogofRule
from bulk_discount import BulkDiscount
from storage import Storage

class Checkout:
    def __init__(self, pricing_rules=[]):
        self.pricing_rules = pricing_rules
        self.basket = []
        self.products = Storage().products

    def scan(self, product_code):
        for product in self.products:
            if product.code == product_code:
                self.basket.append(product)

    def total(self):
        total = sum(item.price for item in self.basket)
        total -= sum(rule(self.basket).discount() for rule in self.pricing_rules)

        return total
