from item import Item

class Storage():
    def __init__(self):
        self.products = [
            Item(name='Fruit Tea', code='FR1', price=3.11),
            Item(name='Strawberries', code='SR1', price=5.00),
            Item(name='Coffee', code='CF1', price=11.23)
        ]

    def add(self, item):
        self.products.append(item)

    def remove(self, item):
        self.products.remove(item)
