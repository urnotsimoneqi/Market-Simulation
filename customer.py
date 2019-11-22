import random
import time
from threading import Thread, Lock

import numpy

from constants import tick_time, seed, high_quality, related_product
from google_ads import GoogleAds
from market import Market
from twitter import Twitter
import logging
import math

random.seed(seed)


class Customer(object):

    def __init__(self, id, type, name, email, wallet, tolerance):
        self.id, self.type, self.name, self.email, self.wallet, self.tolerance = id, type, name, email, wallet, tolerance
        logging.info("[Buyer]:Buyer %s Initialized", self.name)

        # Register the user with google ads
        GoogleAds.register_user(self)

        # ad space stores all the adverts consumed by this user
        self.ad_space = set()
        # stores all the bought products
        self.owned_products = set()

        # flag to stop thread
        self.STOP = False

        # regulate synchronisation
        self.lock = Lock()
        self.tick_count = 0

        # start this user in separate thread
        self.thread = Thread(name=name, target=self.loop)
        self.thread.start()

    # View the advert to this consumer. The advert is appended to the ad_space
    def view_advert(self, product):
        self.lock.acquire()
        self.ad_space.add(product)
        self.lock.release()

    # Consumer decided to buy a 'product'.
    def buy(self, products):
        # enable buyer to buy more than one products
        amount = 0
        for product in products:
            amount += product.stock_price
            # logging.info("[Customer]: (%s,%d) buy the Products:[%s] from seller%s", self.name, self.tick_count, product.product_name, product.seller_id)
        # if not enough money in wallet, don't proceed
        if self.wallet < amount:  # enable buyer to buy more than one products
            return
        test = ', '.join(x.product_name for x in products)
        logging.info("[Customer]: (%s,%d) buy the Products:[%s] from seller%s with price%d", self.name, self.tick_count,
                     test, product.seller_id, amount)
        # purchase the product from market
        # add amount as parameter
        Market.buy(self, products)

        # add product to the owned products list
        for product in products:
            self.owned_products.add(product)

    # money is deducted from user's wallet when purchase is completed
    def deduct(self, money):
        self.wallet -= money

    # User expresses his sentiment about the product on twitter
    def tweet(self, product, sentiment):
        Twitter.post(self, product, sentiment)

    # Loop function to keep the simulation going
    def loop(self):
        logging.info("[Customer]:Customer %s entered Trading", self.name)
        while not self.STOP:
            self.tick_count += 1
            logging.info("[Customer]:(%s,%d): Next Quarter Begins ", self.name, self.tick_count)
            self.tick()
            time.sleep(tick_time)
            test = ', '.join(x.product_name for x in self.owned_products)
            logging.info("[Customer]: (%s,%d) own the Products:[%s] with balance of $ %d", self.name, self.tick_count,
                         test, self.wallet)
        logging.info("[Customer]: (%s,%d) Exit", self.name, self.tick_count)

    # one timestep in the simulation world
    def tick(self):
        test = ', '.join(x.product_name + " from Seller " + str(x.seller_id) for x in self.ad_space)
        logging.info("[Customer]:(%s,%d) currently seeing ads for the Products:[%s]", self.name, self.tick_count, test)
        self.lock.acquire()

        # user looks at all the adverts in his ad_space
        for product in self.ad_space:
            # user checks the reviews about the product on twitter
            tweets = numpy.asarray(Twitter.get_latest_tweets(product, 100))
            user_sentiment = 1 if len(tweets) == 0 else (tweets == 'POSITIVE').mean()
            logging.info("[Customer]:(%s,%d)'s sentiment is %d for product:[%s] from Seller %d", self.name,
                         self.tick_count, user_sentiment, product.product_name, product.seller_id)

            #  Certain buyers prefer items of higher quality
            if self.type == high_quality:
                if product.product_quality < self.tolerance:
                    logging.info("[Customer]: (%s,%d) prefer high quality, so she doesn't buy any products ",
                                 self.name, self.tick_count)
                else:
                    # if sentiment is more than user's tolerance and user does not have the product,
                    # then he/she may buy it with 20% chance.
                    # If it already has the product, then chance of buying again is 1%
                    if user_sentiment >= self.tolerance and ((product not in self.owned_products and random.random() < 0.1) or (product in self.owned_products and random.random() < 0.01)):
                        logging.info("[Customer]:(%s,%d)bought the product:[%s]", self.name, self.tick_count, product.product_name)
                        products= [product, product]
                        self.buy(products)
                    # if user_sentiment >= self.tolerance and (
                    #         (product not in self.owned_products and random.random() < 0.2) or (
                    #         product in self.owned_products and random.random() < 0.01)):
                    #     products = [product, product]
                    #     logging.info("[Customer]:(%s,%d)bought %d product:[%s]", self.name, self.tick_count,
                    #                  len(products), product.product_name)
                    #     self.buy(products)
                    else:
                        logging.info("[Customer]:###(%s,%d)doesn't buy any products ", self.name, self.tick_count)
            #  Buyers are interested in buying related products like a phone and its case in separate transaction.
            #  I.e. if a buyer bought the phone, they are more likely to purchase the case
            elif self.type == related_product:
                products = [product, product]
                self.buy(products)
                # tick_count == 0 represent the customer didn't buy anything
                # if self.tick_count == 0 or self.tick_count == 1:
                #     self.buy([product])
                # else:
                #     for product_bought in self.owned_products:
                #         if if_related_product(product.product_id, product_bought.product_id):
                #             logging.info("[Customer]: (%s,%d) bought product %s, "
                #                          "so he is likely to buy related product %s ",
                #                          self.name, self.tick_count, product_bought.product_name, product.product_name)
                #             self.buy([product])
                #         else:
                #             logging.info("[Customer]: (%s,%d) is interested in buying related products, "
                #                          "so he doesn't buy any products ",
                #                          self.name, self.tick_count)
            else:
                print('Not a valid Customer type')

            # ANSWER d.
            # # if sentiment is more than user's tolerance and user does not have the product, then he/she may buy it with 20% chance. If it already has the product, then chance of buying again is 1%
            # if user_sentiment >= self.tolerance and ((product not in self.owned_products and random.random() < 0.1) or (product in self.owned_products and random.random() < 0.01)):
            #     logging.info("[Customer]:(%s,%d)bought the product:[%s]", self.name, self.tick_count, product.product_name)
            #     self.buy([product])

        # remove the adverts from ad_space
        self.ad_space = set()

        # with some chance, the user may tweet about the product
        if random.random() < 0.5 and len(self.owned_products) > 0:
            # he may choose any random product
            product = random.choice(list(self.owned_products))

            # sentiment in positive if the quality is higher than the tolerance
            sentiment = 'POSITIVE' if self.tolerance < product.product_quality else 'NEGATIVE'

            # tweet sent
            self.tweet(product, sentiment)
            logging.info("[Customer]:(%s,%d) Posted %s tweet for the product %s",
                         self.name, self.tick_count, sentiment, product.product_name)
            # print("with some chance, the user may tweet about the product")
            # print(self.name+product.name+sentiment)

        self.lock.release()

    # set the flag to True and wait for thread to join
    def kill(self):
        self.STOP = True
        self.thread.join(timeout=0)

    def __str__(self):
        return self.name
