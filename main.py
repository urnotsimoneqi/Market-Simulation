import logging
import os
import random
import time
from datetime import datetime

from constants import seed
from mysql import initialize_customer, initialize_seller
from utils import plot

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
    time.sleep(2)
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
for seller in sellers:
    plot(seller)

# print('Total Profit Apple:', seller_apple.my_profit())
# print('Total Profit Samsung:', seller_samsung.my_profit())
for seller in sellers:
    # print('Total Profit:', seller.my_profit())
    print("Seller %s's Total Profit:%d"%(seller.name, seller.my_profit()))

# Kill consumer threads
for consumer in customers:
    consumer.kill()
