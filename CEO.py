from google_ads import GoogleAds
import mysql
import logging

class CEO:
    def __init__(self, seller):
        self.seller = seller

    # Cognition system that decides what to do next.
    def analyze(self, product):
        # WRITE YOUR INTELLIGENT CODE HERE
        # You can use following functions to make decision
        #   my_revenue
        #   my_expenses
        #   my_profit
        #   user_sentiment
        #
        # You need to return the type of advert you want to publish and at what scale
        # GoogleAds.advert_price[advert_type] gives you the rate of an advert
        if GoogleAds.user_coverage(product) < 0.5:
            advert_type = GoogleAds.ADVERT_BASIC
        else:
            advert_type = GoogleAds.ADVERT_TARGETED
        logging.info('[CEO]: (%s,%d) CEO wallet %d ads price %d',
                     self.seller.name, self.seller.tick_count, self.seller.wallet, GoogleAds.advert_price[advert_type])
        scale = self.seller.wallet // GoogleAds.advert_price[advert_type] // 10  # not spending everything
        # scale = 5
        logging.info('[CEO]: (%s,%d) CEO selected advert_type as %s with scale of %d for %s',
                     self.seller.name, self.seller.tick_count, advert_type, scale, product.product_name)
        return advert_type, scale

    def get_most_popular_products(self):
        seller_id = self.seller.id
        product_sales_amount, items_sold, product_id = mysql.find_most_popular_products(seller_id)
        return product_sales_amount, items_sold, product_id

    def purchase_stock(self):
        stocks = mysql.initialize_stock(self.seller.id)
        product_sales_amount, items_sold, product_id = self.get_most_popular_products()

        if product_sales_amount != -1 and product_sales_amount != -1 and items_sold != 1:
            # print('the most popular product', product_sales_amount, items_sold, product_id)
            seller_balance = self.seller.wallet
            product_market_price = mysql.find_product_market_price(product_id)
            items_to_buy = int(seller_balance // product_market_price)
            if self.seller.wallet > 0 and items_to_buy > 0:
                # print('items_to_buy', items_to_buy)
                items_to_buy = 1
                for stock in stocks:
                    if stock.product_id == product_id and stock.stock_quantity < 5:
                        # print('stock', stock.product_id)

                        new_quantity = stock.stock_quantity + items_to_buy
                        new_cost = stock.stock_cost + product_market_price * items_to_buy
                        seller_wallet = self.seller.wallet - new_cost
                        mysql.update_stock(product_id, self.seller.id, new_quantity, new_cost, seller_wallet)
                        self.seller.wallet = seller_wallet

    def adjust_price(self):
        products_sold = None
        most_popular_product_id = -1
        least_popular_product_id = -1

        products_sold = mysql.find_all_products(self.seller.id)

        if products_sold is not None and len(products_sold) != 0:

            if len(products_sold) > 1:
                most_popular_product_id = products_sold[0][0]
                least_popular_product_id = products_sold[-1][0]
            elif products_sold[0][1] > 0:
                most_popular_product_id = products_sold[0][0]
                least_popular_product_id = -1
            else:
                most_popular_product_id = -1
                least_popular_product_id = products_sold[-1][0]

            if most_popular_product_id != -1:
                selling_price = mysql.find_product_selling_price(most_popular_product_id)
                discount = 1.1
                updated_selling_price = selling_price * discount
                mysql.update_product_selling_price(most_popular_product_id, self.seller.id, updated_selling_price)

            if least_popular_product_id != -1:
                selling_price = mysql.find_product_selling_price(least_popular_product_id)
                discount = 0.9
                updated_selling_price = selling_price * discount
                mysql.update_product_selling_price(least_popular_product_id, self.seller.id, updated_selling_price)

    def decide_how_much_to_spend_on_ads(self):
        percentage = 0
        gross_annual_revenue = mysql.get_gross_revenue(self.seller.id)
        if gross_annual_revenue is not None and self.seller.wallet > 200:
            if gross_annual_revenue < 10000:
                percentage = 0.2
            else:
                percentage = 0.075
        ads_cost = percentage * gross_annual_revenue
        return ads_cost

    # increase price for product with least stock in the market
    def check_any_products_out_of_stock(self):
        product_id = mysql.find_the_product_out_of_stock()
        products = mysql.find_all_products(self.seller.id)
        if product_id > 0 and product_id in products:
            multiplier = 1.1
            mysql.increase_product_price(product_id, self.seller.id, 1.1)

    # if seller's wallet is < 200, reduce price for all the products
    def apply_discount_for_all_products(self):
        discount = 0.8
        products = None
        products = mysql.find_all_products(self.seller.id)
        if products is not None:
            mysql.apply_discount_to_all_products(self.seller.id, discount)
