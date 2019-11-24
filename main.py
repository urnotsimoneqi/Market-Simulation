import logging
import os
import random
import time
from datetime import datetime

from constants import seed
# from mysql import initialize_customer, initialize_seller
import mysql
import fuzzy_logic
# from utils import plot
from operator import itemgetter
from sales_summary import SalesSummary
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

# Initialize customers from database
customers = mysql.initialize_customer()

# Initialize sellers with products from database
sellers = mysql.initialize_seller()

# Wait till the simulation ends
try:
    time.sleep(3)
except KeyboardInterrupt:
    pass

# kill seller thread
for seller in sellers:
    seller.kill()

# Plot the sales and expenditure trends
# plot(seller_apple)
# plot(seller_samsung)
# for seller in sellers:
#     plot(seller)

seller_performance = []
dt = datetime.now()
year = dt.year
quarter = (dt.month - 1) // 3 + 1
for seller in sellers:
    # summarize the seller's sales
    revenue = float(mysql.calculate_transaction_revenue(seller.id, year, quarter))
    cost = float(mysql.calculate_total_stock_cost(seller.id))
    expenses = float(seller.my_expenses())
    profit = seller.wallet+revenue-cost-expenses

    print("Seller %s's Total Profit:%d"%(seller.name, seller.my_profit()))
    print("Seller %s's Total Revenue:%d"%(seller.name, seller.my_revenue()))
    print("Seller %s's Total Expense:%d"%(seller.name, seller.my_expenses()))

    grade = fuzzy_logic.fuzzy_logic(revenue, profit)
    seller_performance.append([seller.name, revenue, profit, grade])

    sales_summary = SalesSummary(seller_id=seller.id, sales_year=year, sales_quarter=quarter,
                                 sales_expenses_amount=expenses+cost, sales_revenue=revenue, sales_profit=profit)
    logging.info("[Main]: Seller %s total ads expense is %d, total stock cost is %d, "
                 "total revenue is %d, and total profit is %d",
                 seller.name, expenses, cost, revenue, profit)

    # write sales summary to database
    mysql.save_sales_summary(sales_summary)

seller_performance = sorted(seller_performance, key=itemgetter(3), reverse=True)
# send_email.send_mail(SENDER_ROBOT, RECEIVER_ROBOT, seller_performance, 'NULL')

# Kill consumer threads
for consumer in customers:
    consumer.kill()
