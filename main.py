import random
import time

from constants import seed
from customer import Customer
from product import Product
from seller import Seller
from utils import plot
import os
import logging
from datetime import datetime
from mysql import register_customer

now = datetime.now()
dt_string = now.strftime("%H%M%S_%d_%m_%Y")

if not os.path.exists("log"):
    os.mkdir("log")

logging.basicConfig(filename=os.path.join("log", dt_string+'.log'), level=logging.INFO)

random.seed(seed)

# Create some Consumers
# customers = [Customer(name='consumer_' + str(i), wallet=500, tolerance=0.5 + 0.4 * random.random()) for i in range(10)]
customers = register_customer() # create users from database

# Create a product
iphone = Product(name='iphone', price=300, quality=0.9)
galaxy = Product(name='galaxy', price=200, quality=0.8)

# Create a Seller with some budget
seller_apple = Seller(name='apple', products=[iphone], wallet=1000)
seller_samsung = Seller(name='samsung', products=[galaxy], wallet=500)

# Wait till the simulation ends
try:
    time.sleep(10)
except KeyboardInterrupt:
    pass

# kill seller thread
seller_apple.kill()
seller_samsung.kill()

# Plot the sales and expenditure trends
plot(seller_apple)
plot(seller_samsung)

print('Total Profit Apple:', seller_apple.my_profit())
print('Total Profit Samsung:', seller_samsung.my_profit())

# Kill consumer threads
for consumer in customers:
    consumer.kill()
