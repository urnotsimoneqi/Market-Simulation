#!/usr/bin/python3

from threading import Lock
from google_ads import GoogleAds
import logging
from transaction import Transaction
import datetime
from random import choice
import mysql

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
        # products: list of product of the same type, such as the iPhone XS
        product_id = products[0].product_id
        product_name = products[0].product_name
        product_price = products[0].stock_price
        seller_id = products[0].seller_id
        promotion_id = -1

        most_valuable_customer_id = mysql.find_most_valuable_customer(seller_id)

        # get the seller for product from catalogue
        for product in products:
            # # random choose seller
            # seller_index = choice(Market.catalogue[product.product_name])
            # index = Market.catalogue[product.product_name].index(seller_index)
            # seller = Market.catalogue[product.product_name][index]

            # find seller in the market catalogue
            for x in Market.catalogue.get(product.product_name):
                if x.id == seller_id:
                    seller = x

            # find the buyer who has spent the most in the same seller and offer discount
            if most_valuable_customer_id == buyer.id:
                product_price = product.stock_price * 0.95
                promotion_id = 1

            # call seller's sold function
            seller.sold(product)

            # deduct price from user's balance
            buyer.deduct(product.stock_price)

            # track user
            GoogleAds.track_user_purchase(buyer, product)

        # update the stock of product
        products[0].stock_quantity = products[0].stock_quantity - len(products)
        logging.info("[Market]: Update the stock quantity to %d of product %s of seller %s %d",
                     products[0].stock_quantity, product_name, seller.name, seller_id)
        # update the stock of product in database
        mysql.update_stock(product_id, seller_id, products[0].stock_quantity, products[0].stock_cost, seller.wallet)

        dt = datetime.datetime.now()
        transaction = Transaction(datetime=dt, seller_id=seller.id, customer_id=buyer.id,
                                  product_id=product_id, quantity=len(products),
                                  total_amount=product_price*len(products))
        logging.info("[Market]:Transaction between Seller %s and Customer %s with the product %s at %s "
                     "in year %s and quarter %s",
                     seller.name, buyer.name, product_name, transaction.timestamp, transaction.year, transaction.quarter)

        if promotion_id != -1:
            transaction.set_promotion_id(promotion_id)

        if transaction.total_amount >= 2000:
            transaction.total_amount -= 50
            if promotion_id == -1:
                transaction.set_promotion_id(5)

        # write to database
        mysql.save_txn(transaction)