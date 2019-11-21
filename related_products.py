class RelatedProducts:
    def __init__(self, name, related_products, discount=1):
        self.name = name
        self.related_products = related_products
        self.num_of_items = len(related_products)
        self.amount = 0
        for product in related_products:
            self.amount += product.price * discount
