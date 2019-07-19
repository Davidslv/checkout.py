class BulkDiscount:
    def __init__(self, basket):
        self.basket = basket

    def discount(self):
        item_code = 'SR1'
        items = 0

        for item in self.basket:
            if item_code == item.code:
                items += 1

        if (items < 3):
            return 0

        return items * 0.5
