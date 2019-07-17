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
