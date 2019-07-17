class BogofRule:
    def __init__(self, basket):
        self.basket = basket

    def discount(self):
        item_code = 'FR1'
        items = 0
        t_item = None

        for item in self.basket:
            if item_code in item.code:
                t_item = item
                items += 1

        if (items < 2):
            return 0

        return (items // 2) * t_item.price
