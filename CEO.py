from threading import Lock

from google_ads import GoogleAds
import mysql

class CEO:
    def __init__(self, seller):
        self.seller = seller

    # Cognition system that decides what to do next.
    def analyze(self):
        # WRITE YOUR INTELLIGENT CODE HERE
        # You can use following functions to make decision
        #   my_revenue
        #   my_expenses
        #   my_profit
        #   user_sentiment
        #
        # You need to return the type of advert you want to publish and at what scale
        # GoogleAds.advert_price[advert_type] gives you the rate of an advert
        for product in self.seller.products:
            advert_type = GoogleAds.ADVERT_BASIC if GoogleAds.user_coverage(
                product) < 0.5 else GoogleAds.ADVERT_TARGETED
        scale = self.seller.wallet // GoogleAds.advert_price[advert_type] // 2  # not spending everything
        return advert_type, scale

    def get_most_popular_products(self):
        seller_id = self.seller.id
        product_sales_amount, items_sold, product_id = mysql.find_most_popular_products(seller_id)
        return product_sales_amount, items_sold, product_id

    def purchase_stock(self):
        product_sales_amount, items_sold, product_id = self.get_most_popular_products()
        if product_sales_amount != -1 and product_sales_amount != -1 and items_sold != 1:
            print('the most popular product', product_sales_amount, items_sold, product_id)
