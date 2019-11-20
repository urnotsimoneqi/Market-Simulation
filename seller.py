import time
from threading import Lock, Thread

import numpy

from CEO import CEO
from constants import tick_time
from google_ads import GoogleAds
from market import Market
from twitter import Twitter
import logging


class Seller(object):

    def __init__(self, name, products, wallet):
        self.name = name
        self.products = products  # enable seller to sell more than one products
        self.wallet = wallet
        self.count = 0
        logging.info("[Seller]:Seller %s Created", self.name)

        # register the seller in market
        Market.register_seller(self, products)

        # metrics tracker
        self.sales_history = []
        self.revenue_history = []
        self.profit_history = []
        self.expense_history = [0]
        self.sentiment_history = []
        self.item_sold = 0

        # Flag for thread
        self.STOP = False

        self.lock = Lock()

        # start this seller in separate thread
        self.thread = Thread(name=name, target=self.loop)
        self.thread.start()

    def loop(self):
        while not self.STOP:
            self.count += 1
            self.tick()
            time.sleep(tick_time)

    # if an item is sold, add it to the database
    def sold(self):
        self.lock.acquire()
        self.item_sold += 1
        self.lock.release()

    # one timestep in the simulation world
    def tick(self):
        self.lock.acquire()

        # append the sales record to the history
        self.sales_history.append(self.item_sold)

        # reset the sales counter
        self.item_sold = 0

        self.lock.release()

        # Calculate the metrics for previous tick and add to tracker
        for product in self.products:
            self.revenue_history.append(self.sales_history[-1] * product.price)
            self.profit_history.append(self.revenue_history[-1] - self.expense_history[-1])
            self.sentiment_history.append(self.user_sentiment())

        # add the profit to seller's wallet
        self.wallet += self.my_profit(True)

        # choose what to do for next timestep
        advert_type, scale = CEO(self).analyze()

        # ANSWER a. print data to show progress
        print('Revenue in previous quarter:', self.my_revenue(True))
        print('Expenses in previous quarter:', self.my_expenses(True))
        print('Profit in previous quarter:', self.my_profit(True))
        print('\nStrategy for next quarter \nAdvert Type: {}, scale: {}\n\n'.format(advert_type, scale))

        logging.info('[Seller]: (%s,%d) Revenue in previous quarter:%d', self.name, self.count, self.my_revenue(True))
        logging.info('[Seller]: (%s,%d) Expenses in previous quarter:%d', self.name, self.count, self.my_expenses(True))
        logging.info('[Seller]: (%s,%d) Profit in previous quarter:%d', self.name, self.count, self.my_profit(True))

        # perform the actions and view the expense
        for product in self.products:
            self.expense_history.append(GoogleAds.post_advertisement(self, product, advert_type, scale))

    # calculates the total revenue. Gives the revenue in last tick if latest_only = True
    def my_revenue(self, latest_only=False):
        revenue = self.revenue_history[-1] if latest_only else numpy.sum(self.revenue_history)
        return revenue

    # calculates the total revenue. Gives the revenue in last tick if latest_only = True
    def my_expenses(self, latest_only=False):
        bill = self.expense_history[-1] if latest_only else numpy.sum(self.expense_history)
        return bill

    # calculates the total revenue. Gives the revenue in last tick if latest_only = True
    def my_profit(self, latest_only=False):
        profit = self.profit_history[-1] if latest_only else numpy.sum(self.profit_history)
        return profit

    # calculates the user sentiment from tweets.
    def user_sentiment(self):
        for product in self.products:
            tweets = numpy.asarray(Twitter.get_latest_tweets(product, 100))
        return 1 if len(tweets) == 0 else (tweets == 'POSITIVE').mean()

    # to stop the seller thread
    def kill(self):
        self.STOP = True
        self.thread.join()

    def __str__(self):
        return self.name

