class Product(object):
    def __init__(self, product_id, name, market_price, quality, quantity):
        assert quality <= 1

        self.product_id = product_id
        self.name = name
        self.market_price = market_price
        self.quality = quality
        self.quantity = quantity  # num of products
