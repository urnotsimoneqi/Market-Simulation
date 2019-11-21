class Product(object):
    def __init__(self, product_id, name, price, quality, quantity):
        assert quality <= 1

        self.product_id = product_id
        self.name = name
        self.price = price
        self.quality = quality
        self.quantity = quantity  # num of products
