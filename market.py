from threading import Lock

from google_ads import GoogleAds
import logging

# from mysql import save_txn
from transaction import Transaction
import time

class Market(object):
    catalogue = {}
    lock = Lock()

    # initialise the seller catalogue
    @staticmethod
    def register_seller(seller, products):
        Market.lock.acquire()
        for product in products:
            # the product has not been added to the catalogue
            if product.product_name not in Market.catalogue.keys():
                Market.catalogue[product.product_name] = [seller]
            # the product has been added to the catalogue, append seller
            elif product.product_name in Market.catalogue.keys():
                # enable multiple sellers to sell the same product
                Market.catalogue[product.product_name].append(seller)
            else:
                print("Error")
            logging.info("[Market]:Seller %s is registered in the market with the product %s ",
                         seller.name, product.product_name)
        Market.lock.release()

    # when a user buys a product, increment the seller's sales
    @staticmethod
    def buy(buyer, products):
        # products: list of product of the same type
        product_id = products[0].product_id
        product_name = products[0].product_name
        product_price = products[0].stock_price
        # get the seller for product from catalogue
        for product in products:
            seller = Market.catalogue[product.product_name][0]  # need to revise, choose the first seller by default

            # call seller's sold function
            seller.sold(product)

            # deduct price from user's balance
            buyer.deduct(product.stock_price)

            # track user
            GoogleAds.track_user_purchase(buyer, product)

        # write to database
        # format YYYY-MM-DD HH:MM:SS
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        transaction = Transaction(timestamp=timestamp, seller_id=seller.id, customer_id=buyer.id,
                                  product_id=product_id, quantity=len(products),
                                  total_amount=product_price*len(products))
        logging.info("[Market]:Transaction between Seller %s and Customer %s with the product %s ",
                     seller.name, buyer.name, product_name)
        # save_txn()

