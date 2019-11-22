class Stock(object):
    def __init__(self, product_id, product_name, product_market_price, product_quality, product_status, seller_id,
                 stock_quantity, stock_cost, stock_price):
        self.product_id = product_id
        self.product_name = product_name
        self.market_price = product_market_price
        self.product_quality = product_quality
        self.product_status = product_status
        self.seller_id = seller_id
        self.stock_quantity = stock_quantity
        self.stock_cost = stock_cost
        self.stock_price = stock_price
