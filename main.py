import logging
import os
import random
import sys
import threading
import time
from datetime import datetime

from constants import seed
# from mysql import initialize_customer, initialize_seller
import mysql
import fuzzy_logic
# from utils import plot
from operator import itemgetter
from sales_summary import SalesSummary
from product_summary import ProductSummary
import send_email
import report

SENDER_ROBOT = 'a0198900xrobot@gmail.com'
RECEIVER_ROBOT = 'a0198900xreceiver@gmail.com'
PASSWORD = 'A0198900X'

now = datetime.now()
dt_string = now.strftime("%H%M%S_%d_%m_%Y")

if not os.path.exists("log"):
    os.mkdir("log")

logging.basicConfig(filename=os.path.join("log", dt_string+'.log'), level=logging.INFO)

random.seed(seed)

# Initialize customers from database
customers = mysql.initialize_customer()

# Initialize sellers with products from database
sellers = mysql.initialize_seller()

# Initialize products in the market
products = mysql.initialize_product()

seller_cost_dict = {}
for seller in sellers:
    cost = mysql.calculate_total_stock_cost(seller.id)
    seller_cost_dict[seller.id] = cost

# Wait till the simulation ends
try:
    time.sleep(3)
except KeyboardInterrupt:
    pass

# kill seller thread
for seller in sellers:
    seller.kill()

# Kill consumer threads
for consumer in customers:
    consumer.kill()

# calculate seller performance
seller_performance = []
dt = datetime.now()
year = dt.year
quarter = (dt.month - 1) // 3 + 1
for seller in sellers:
    # summarize the seller's sales
    revenue = float(mysql.calculate_transaction_revenue(seller.id, year, quarter))
    # cost = float(mysql.calculate_total_stock_cost(seller.id))
    expenses = float(seller.my_expenses())
    # profit = seller.wallet+revenue-cost-expenses
    cost = seller_cost_dict[seller.id]
    profit = revenue-cost-expenses

    # print("Seller %s's Total Profit:%d"%(seller.name, seller.my_profit()))
    # print("Seller %s's Total Revenue:%d"%(seller.name, seller.my_revenue()))
    # print("Seller %s's Total Expense:%d"%(seller.name, seller.my_expenses()))

    mysql.update_seller_wallet(seller.id, profit)

    grade = fuzzy_logic.fuzzy_logic(revenue, profit)
    seller_performance.append([seller.name, revenue, profit, grade])

    # update seller's sales summary
    sales_summary = SalesSummary(seller_id=seller.id, sales_year=year, sales_quarter=quarter,
                                 sales_expenses_amount=expenses+cost, sales_revenue=revenue, sales_profit=profit)
    logging.info("[Main]: Seller %s total ads expense is %d, total stock cost is %d, "
                 "total revenue is %d, and total profit is %d",
                 seller.name, expenses, cost, revenue, profit)

    # write sales summary to database
    mysql.save_sales_summary(sales_summary)

seller_performance = sorted(seller_performance, key=itemgetter(3), reverse=True)
if len(seller_performance) > 2:
    seller_performance = seller_performance[0:3]

# write product summary into database
for product in products:
    product_summary = mysql.extract_product_summary(product.product_id, 4)
    if product_summary is not None:
        mysql.save_product_summary(product_summary)

# Send email to customer
for customer in customers:
    pass
    # report.send_customer_email(customer.id, SENDER_ROBOT, customer.email, seller_performance)

# Send email until the report being generated
file_path = "report.jpg"
while not os.path.exists(file_path):
    try:
        time.sleep(10)
        print("File does not exist, wait...")
    except KeyboardInterrupt:
        pass
if os.path.isfile(file_path):
    print("Read file")
    for seller in sellers:
        pass
        # report.send_seller_email(seller.name, SENDER_ROBOT, RECEIVER_ROBOT, file_path)

    # kill the main thread
    if threading.current_thread().name == 'MainThread':
        try:
            # sys.exit(0)
            os._exit(0)
        except Exception as e:
            print(e)
            print('Program is dead.')
        finally:
            print('clean-up')
else:
    raise ValueError("%s isn't a file!" % file_path)
