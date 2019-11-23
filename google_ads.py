import random
from collections import defaultdict
from threading import Lock

from constants import seed
import logging
import json

random.seed(seed)


class GoogleAds(object):
    # Define the types of adverts available
    ADVERT_BASIC = 'BASIC'
    ADVERT_TARGETED = 'TARGETED'

    # Define advert's price
    advert_price = {
        ADVERT_BASIC: 100,
        ADVERT_TARGETED: 200
    }

    # Google's internal database
    users = []
    expenses = defaultdict(list)
    purchase_history = defaultdict(list)

    lock = Lock()

    # post an advert about the product
    @staticmethod
    def post_advertisement(seller, product, advert_type, scale):
        # scale of adverts should not be more than number of users
        # users = list(set(GoogleAds.users))  # Remove duplicate elements in list
        users = list(GoogleAds.users)
        scale = min(int(scale), len(users))  # convert scale to integer type
        GoogleAds.lock.acquire()

        # if advert_type is basic, choose any set of customers
        if advert_type == GoogleAds.ADVERT_BASIC:
            users = random.choices(GoogleAds.users, k=scale)
            users = list(set(users))
            users_str = ', '.join(x.name for x in users)
            logging.info('[GoogleAds]: Google pushed the %s Ad for product %s of seller %d to users %s ',
                         advert_type, product.product_name, product.seller_id, users_str)
        # if advert_type is targeted, choose user's who were not shown the same advert in previous tick
        elif advert_type == GoogleAds.ADVERT_TARGETED:
            new_users = list(set(GoogleAds.users) - set(GoogleAds.purchase_history[product]))
            if new_users:  # if list of new_users is not null
                users = random.choices(new_users, k=scale)
                users = list(set(users))
                users_str = ', '.join(x.name for x in users)
                logging.info('[GoogleAds]: Google pushed the %s Ad for product %s of seller %d to user %s ',
                         advert_type, product.product_name, product.seller_id, users_str)
            else:
                print("new_users list is null")
        else:
            print('Not a valid Advert type')
            return

        # publish the advert to selected user
        scale = len(users)
        for user in users:
            user.view_advert(product)

        # update the bill into seller's account
        bill = scale * GoogleAds.advert_price[advert_type]
        GoogleAds.expenses[seller].append(bill)
        # data = json.loads(json.dumps(GoogleAds.expenses))
        # logging.info('[GoogleAds]: Google billed the Seller %s  ', data)
        GoogleAds.lock.release()

        # return the bill amount to the seller
        return bill

    @staticmethod
    def register_user(user):
        GoogleAds.lock.acquire()
        GoogleAds.users.append(user)
        # logging.info("[GoogleAds]:Customer %s added to Google list of user with Tolerance:%s",
        # user.name, user.tolerance)
        GoogleAds.lock.release()

    @staticmethod
    def track_user_purchase(user, product):
        GoogleAds.lock.acquire()
        GoogleAds.purchase_history[product].append(user)
        GoogleAds.lock.release()

    @staticmethod
    def user_coverage(product):
        # purchase_history = ', '.join(x.name for x in GoogleAds.purchase_history[product])
        # print("purchase history"+str(len(GoogleAds.purchase_history[product])))
        # print("purchase history"+purchase_history)
        return len(set(GoogleAds.purchase_history[product])) / len(GoogleAds.users)
