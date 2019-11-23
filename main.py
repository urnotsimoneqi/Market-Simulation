import logging
import os
import random
import time
from datetime import datetime

from constants import seed
from fuzzy_logic import fuzzy_logic
from mysql import initialize_customer, initialize_seller
# from utils import plot
from operator import itemgetter
import send_email

SENDER_ROBOT = 'a0198900xrobot@gmail.com'
RECEIVER_ROBOT = 'a0198900xreceiver@gmail.com'
PASSWORD = 'A0198900X'


now = datetime.now()
dt_string = now.strftime("%H%M%S_%d_%m_%Y")

if not os.path.exists("log"):
    os.mkdir("log")

logging.basicConfig(filename=os.path.join("log", dt_string+'.log'), level=logging.INFO)

random.seed(seed)

# Create some Consumers
# customers = [Customer(name='consumer_' + str(i), wallet=500, tolerance=0.5 + 0.4 * random.random()) for i in range(5)]
customers = initialize_customer() # create users from database

# Create a product
# iphone = Product(name='iphone', price=300, quality=0.9)
# galaxy = Product(name='galaxy', price=200, quality=0.8)
# products = initialize_product(1)

# Create a Seller with some budget
# seller_apple = Seller(name='apple', products=[iphone], wallet=1000)
# seller_samsung = Seller(name='samsung', products=[galaxy], wallet=500)
sellers = initialize_seller()

# Wait till the simulation ends
try:
    time.sleep(3)
except KeyboardInterrupt:
    pass

# kill seller thread
# seller_apple.kill()
# seller_samsung.kill()
for seller in sellers:
    seller.kill()

# Plot the sales and expenditure trends
# plot(seller_apple)
# plot(seller_samsung)
# for seller in sellers:
#     plot(seller)

# print('Total Profit Apple:', seller_apple.my_profit())
# print('Total Profit Samsung:', seller_samsung.my_profit())
seller_performance = []
for seller in sellers:
    grade = fuzzy_logic(seller.my_revenue(), seller.my_profit())
    print("Seller %s's Total Profit:%d"%(seller.name, seller.my_profit()))
    print("Seller %s's Total Revenue:%d"%(seller.name, seller.my_revenue()))
    print("Seller %s's Total Expense:%d"%(seller.name, seller.my_expenses()))
    seller_performance.append([seller.name, seller.my_revenue(), seller.my_profit(), grade])

seller_performance = sorted(seller_performance, key=itemgetter(3), reverse=True)
# send_email.send_mail(SENDER_ROBOT, RECEIVER_ROBOT, seller_performance, 'NULL')

# Kill consumer threads
for consumer in customers:
    consumer.kill()
