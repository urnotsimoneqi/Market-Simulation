from collections import defaultdict
import logging


class Twitter(object):
    # dictionary to store tweets
    feed = defaultdict(list)

    # Called by the user to tweet something
    @staticmethod
    def post(user, product, tweet):
        Twitter.feed[product].append((user, tweet))
        for product, reviews in Twitter.feed.items():
            logging.info("[Twitter]: Reviews for product %s of seller %d: %s",
                         product.product_name, product.seller_id, str(reviews))
            # print(product.product_name+","+str(reviews))

    # returns the latest tweet about a product.
    @staticmethod
    def get_latest_tweets(product, n):
        return [tweet for user, tweet in Twitter.feed[product][-n:]]
