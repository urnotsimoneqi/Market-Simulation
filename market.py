from threading import Lock

from google_ads import GoogleAds


class Market(object):
    catalogue = {}
    lock = Lock()

    # initialise the seller catalogue
    @staticmethod
    def register_seller(seller, products):
        Market.lock.acquire()
        for product in products:
            Market.catalogue[product] = seller  # enable seller to sell more than one products
        Market.lock.release()

    # when a user buys a product, increment the seller's sales
    @staticmethod
    def buy(buyer, products):
        # get the seller for product from catalogue
        for product in products:
            seller = Market.catalogue[product]

            # call seller's sold function
            seller.sold()

            # deduct price from user's balance
            buyer.deduct(product.stock_price)

            # track user
            GoogleAds.track_user_purchase(buyer, product)
