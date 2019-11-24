#!/usr/bin/python3

import pymysql
from customer import Customer
from seller import Seller
from stock import Stock
from product import Product
from product_summary import ProductSummary


# set up your information here to connect to mysql
def connect_db():
    db = pymysql.connect("localhost", "root", "Simon19980908", "TESTDB")
    return db


# initialize customers
def initialize_customer():
    customers = []
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT * FROM customer"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            customer_id = row[0]
            customer_type = row[1]
            customer_name = row[2]
            customer_email = row[3]
            customer_wallet = row[4]
            customer_tolerance = row[5]
            customer_status = row[6]
            customer = Customer(id=customer_id, type=customer_type, name=customer_name, email=customer_email,
                                wallet=customer_wallet, tolerance=customer_tolerance)
            customers.append(customer)
    except Exception as e:
        print(e)
    db.close()
    return customers


# initialize certain seller's stock
def initialize_stock(seller_id):
    stock_list = []
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT a.product_id, a.product_name, a.product_market_price, a.product_status, " \
          "b.seller_id, b.product_quality, b.stock_quantity, b.stock_cost, b.stock_price FROM " \
          "product AS a,stock AS b where a.product_id=b.product_id and b.seller_id= " + str(seller_id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            product_id = row[0]
            product_name = row[1]
            product_market_price = row[2]
            product_status = row[3]

            seller_id = row[4]
            product_quality = row[5]
            stock_quantity = row[6]
            stock_cost = row[7]
            stock_price = row[8]
            stock = Stock(product_id=product_id, product_market_price=product_market_price, product_name=product_name,
                          product_quality=product_quality,
                          product_status=product_status, seller_id=seller_id, stock_quantity=stock_quantity,
                          stock_cost=stock_cost, stock_price=stock_price)
            stock_list.append(stock)
    except Exception as e:
        print(e)
    db.close()
    return stock_list


# initialize sellers with products
def initialize_seller():
    sellers = []
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT * FROM seller"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            seller_id = row[0]
            seller_name = row[1]
            seller_wallet = row[2]
            seller_status = row[3]
            seller_products = initialize_stock(seller_id)
            seller = Seller(id=seller_id, name=seller_name, products=seller_products, wallet=seller_wallet)
            sellers.append(seller)
    except Exception as e:
        print(e)
    db.close()
    return sellers


def reporting(revenue, expenses, profit):
    db = connect_db()
    # db = pymysql.connect("localhost", "root", "Simon19980908", "TESTDB")

    db.close()


# insert every transaction into database
def save_txn(txn):
    db = connect_db()
    cursor = db.cursor()

    sql = "INSERT INTO transaction (transaction_datetime, transaction_year, transaction_quarter, seller_id, customer_id, \
                             product_id, \
                             transaction_quantity, transaction_amount, promotion_id) \
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (txn.timestamp, txn.year, txn.quarter, txn.seller_id, txn.customer_id, txn.product_id,
           txn.quantity, txn.total_amount, txn.promotion_id)
    try:
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        print(e)
        # Rollback in case there is any error
        db.rollback()
    cursor.close()
    db.close()


# related product
def if_related_product(product_id1, product_id2):
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT * FROM related_product where related_product_id1=" + str(product_id1) \
          + " and related_product_id2=" + str(product_id2)

    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            return True
    except Exception as e:
        print(e)
        print("Error: unable to fetch related_product")
    db.close()


def initialize_promotions():
    promotions = []
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT * FROM promotion"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            promotion_id = row[0]
            promotion_discount = row[1]
            promotion = promotion(promotion_id, promotion_discount)
            promotions.append(promotion)
    except Exception as e:
        print(e)
    db.close()
    return promotions


def find_most_popular_products(seller_id):
    db = connect_db()
    cursor = db.cursor()
    product_sales_amount = -1
    product_id = -1
    items_sold = -1

    sql = "select sum(transaction_amount), count(*), product_id from transaction where seller_id = " + str(
        seller_id) + " group by product_id order by count(*) desc limit 1;"
    try:
        cursor.execute(sql)
        results = None
        results = cursor.fetchall()
        if results is None:
            print(seller_id, 'null')
        else:
            for row in results:
                product_sales_amount = row[0]
                items_sold = row[1]
                product_id = row[2]
    except Exception as e:
        print(e)
    db.close()
    return product_sales_amount, items_sold, product_id


def find_product_market_price(product_id):
    db = connect_db()
    cursor = db.cursor()
    market_price = -1

    sql = "select product_market_price from product where product_id = " + str(product_id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if results is None:
            print(product_id, 'null')
        else:
            for row in results:
                market_price = row[0]
    except Exception as e:
        print(e)
        print("Error: unable to fetch market_price from product")
    db.close()
    return market_price


def find_product_market_price(product_id):
    db = connect_db()
    cursor = db.cursor()
    market_price = -1

    sql = "select product_market_price from product where product_id = " + str(product_id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if results is None:
            print(product_id, 'null')
        else:
            for row in results:
                market_price = row[0]
    except Exception as e:
        print(e)
        print("Error: unable to fetch market_price from product")
    db.close()
    return market_price


def update_stock(product_id, seller_id, stock_quantity, stock_cost, seller_wallet):
    db = connect_db()
    cursor = db.cursor()
    sql1 = "UPDATE stock set stock_quantity = " + str(stock_quantity) \
           + " WHERE product_id = " + str(product_id) + " AND seller_id = " + str(seller_id)
    sql2 = "UPDATE seller set seller_wallet = " + str(seller_wallet) + " WHERE seller_id = " + str(seller_id)
    try:
        cursor.execute(sql1)
        db.commit()

        cursor.execute(sql2)
        db.commit()
    except Exception as e:
        print(e)
        print("Error: unable to update stock from product purchase")
    db.close()


def find_all_products(seller_id):
    db = connect_db()
    cursor = db.cursor()
    products = []

    sql = "select product_id, sum(transaction_quantity) from transaction where customer_id = " + str(seller_id) \
          + " group by product_id order by sum(transaction_quantity) desc;"

    try:
        cursor.execute(sql)
        results = None
        results = cursor.fetchall()
        if results is None:
            print(seller_id, 'null')
        else:
            for row in results:
                product_id = row[0]
                items_sold = int(row[1])
                products.append([product_id, items_sold])
    except Exception as e:
        print(e)
        print("Error: unable to fetch all products sold by a seller")
    db.close()
    # print(products)
    return products


def find_product_selling_price(product_id):
    db = connect_db()
    cursor = db.cursor()
    selling_price = -1

    sql = "select stock_price from stock where product_id = " + str(product_id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if results is None:
            print(product_id, 'null')
        else:
            for row in results:
                selling_price = row[0]
    except Exception as e:
        print(e)
        print("Error: unable to fetch market_price from product")
    db.close()
    return selling_price


def update_product_selling_price(product_id, seller_id, selling_price):
    db = connect_db()
    cursor = db.cursor()

    sql1 = "UPDATE stock set stock_price = " + str(selling_price) \
           + " WHERE product_id = " + str(product_id) + " AND seller_id = " + str(seller_id)

    try:
        cursor.execute(sql1)
        db.commit()
    except Exception as e:
        print(e)
        print("Error: unable to update product selling price")
    db.close()


def apply_discount_to_all_procducts(seller_id, discount):
    db = connect_db()
    cursor = db.cursor()

    sql1 = "update stock set stock_price = (stock_price * " + str(discount) + " where seller_id = " + str(seller_id)

    try:
        cursor.execute(sql1)
        db.commit()
    except Exception as e:
        print(e)
        print("Error: unable to apply discount for all products of a seller")
    db.close()


def find_most_valuable_customer(seller_id):
    db = connect_db()
    cursor = db.cursor()
    customer_id = None

    sql = "select customer_id from transaction where seller_id = " \
          + str(seller_id) + " group by customer_id order by sum(transaction_amount) desc limit 1;"

    try:
        cursor.execute(sql)
        results = None
        results = cursor.fetchall()
        if results is None:
            print(seller_id, 'null')
        else:
            for row in results:
                customer_id = row[0]
    except Exception as e:
        print(e)
        print("Error: unable to find the most valuable customer sold by a seller")
    db.close()
    return customer_id


def get_gross_revenue(seller_id):
    db = connect_db()
    cursor = db.cursor()
    gross_revenue = None

    sql = "select sum(transaction_amount) from transaction where seller_id = " + str(seller_id)

    try:
        cursor.execute(sql)
        results = None
        results = cursor.fetchall()
        if results is None:
            print(seller_id, 'null')
        else:
            for row in results:
                gross_revenue = row[0]
    except Exception as e:
        print(e)
        print("Error: unable to find the gross revenue of a seller")
    db.close()
    return gross_revenue


def find_the_product_out_of_stock():
    db = connect_db()
    cursor = db.cursor()
    product_id = -1

    sql = "select product_id, sum(stock_quantity) from stock group by product_id order by sum(stock_quantity) asc limit 1"

    try:
        cursor.execute(sql)
        results = None
        results = cursor.fetchall()
        if results is None:
            print(product_id, 'null')
        else:
            for row in results:
                product_id = row[0]
    except Exception as e:
        print(e)
        print("Error: unable to find the product out of stock")
    db.close()
    return product_id


def increase_product_price(product_id, seller_id, multiplier):
    db = connect_db()
    cursor = db.cursor()

    sql = "UPDATE stock set stock_price = stock_price * " + str(multiplier) \
          + " WHERE product_id = " + str(product_id) \
          + " and seller_id = " + str(seller_id)

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        print("Error: unable to increase product selling price")
    db.close()


def select_sales_summary(seller_id, quarter):
    db = connect_db()
    cursor = db.cursor()

    sql = "select * from sales_summary where seller_id=" + str(seller_id) + " and sales_quarter="+str(quarter)

    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is not None:
            return True
        else:
            return False
    except Exception as e:
        print(e)
    cursor.close()
    db.close()


# insert sales summary into database
def save_sales_summary(sales_summary):
    db = connect_db()
    cursor = db.cursor()

    flag = select_sales_summary(sales_summary.seller_id, sales_summary.sales_quarter)

    if flag:
        sql = "UPDATE sales_summary set sales_expense_amount = " + str(sales_summary.sales_expenses_amount) \
              + ", sales_revenue = " + str(sales_summary.sales_revenue) \
              + ", sales_profit=" + str(sales_summary.sales_profit) \
              + " where seller_id = " + str(sales_summary.seller_id) \
              + " and sales_quarter =" + str(sales_summary.sales_quarter)
    else:

        sql = "INSERT INTO sales_summary (seller_id, sales_year, sales_quarter, " \
          "sales_expense_amount, sales_revenue, sales_profit) VALUES (%s, %s, %s, %s, %s, %s)"

        sql = sql % (sales_summary.seller_id, sales_summary.sales_year, sales_summary.sales_quarter,
                 sales_summary.sales_expenses_amount, sales_summary.sales_revenue, sales_summary.sales_profit)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        # Rollback in case there is any error
        db.rollback()
    cursor.close()
    db.close()


# calculate revenue from transaction table for one quarter in a year
def calculate_transaction_revenue(seller_id, year, quarter):
    db = connect_db()
    cursor = db.cursor()

    sql = "SELECT SUM(transaction_amount) FROM transaction " \
          "where seller_id=%s and transaction_year=%s and transaction_quarter=%s"

    try:
        cursor.execute(sql, (seller_id, year, quarter))
        result = cursor.fetchone()
        if result is not None and len(result) > 0:
            amount = result[0]
            if amount is not None:
                # print("The seller"+str(seller_id)+"'s revenue is "+str(amount))
                return amount
            else:
                return 0
        else:
            return 0
    except Exception as e:
        print(e)
    db.close()


# calculate cost from stock table
def calculate_total_stock_cost(seller_id):
    db = connect_db()
    cursor = db.cursor()
    cost = 0

    sql = "SELECT SUM(stock_quantity*stock_cost) FROM stock " \
          "where seller_id=%s"

    try:
        cursor.execute(sql, seller_id)
        result = cursor.fetchone()
        cost = result[0]  # revenue

    except Exception as e:
        print(e)
    db.close()
    return cost


# count the number of promotions applied as per year and quarter
def find_effective_promotions_per_quarter():
    db = connect_db()
    cursor = db.cursor()
    promotions_used_per_quarter = []

    sql = "select transaction_year, transaction_quarter, promotion_id, count(*) from transaction where promotion_id > 0 group by transaction_year, transaction_quarter, promotion_id order by transaction_year, transaction_quarter, promotion_id;"

    try:
        cursor.execute(sql)
        results = None
        results = cursor.fetchall()
        if results is None:
            print('promotion', 'null')
        else:
            for row in results:
                year = row[0]
                quarter = row[1]
                promotion_id = row[2]
                count = row[3]
                promotions_used_per_quarter.append([year, quarter, promotion_id, count])

    except Exception as e:
        print(e)
        print("Error: unable to find the effective promotions")
    db.close()

    return promotions_used_per_quarter


# update seller wallet
def update_seller_wallet():
    pass


# initialize product
def initialize_product():
    products = []
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT * FROM product"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            product_id = row[0]
            name = row[1]
            market_price = row[2]
            product = Product(product_id=product_id, name=name, market_price=market_price)
            products.append(product)
    except Exception as e:
        print(e)
    db.close()
    return products


# extract product summary from transaction table
def extract_product_summary(product_id, quarter):
    db = connect_db()
    cursor = db.cursor()

    sql = "select transaction_year, transaction_quarter, sum(transaction_quantity) from transaction " \
          "where product_id = " + str(product_id) + " and transaction_quarter=" + str(quarter)

    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is not None:
            product_year = result[0]
            product_quarter = result[1]
            product_counter = result[2]
            product_summary = ProductSummary(product_id=product_id, product_year=product_year,
                                             product_quarter=product_quarter, product_counter=product_counter)
            return product_summary
        else:
            return
    except Exception as e:
        print(e)
    cursor.close()
    db.close()


def save_product_summary(product_summary):
    db = connect_db()
    cursor = db.cursor()

    flag = select_product_summary(product_summary.product_id, product_summary.product_quarter)
    if flag:
        sql = "UPDATE product_summary set product_counter = " + str(product_summary.product_counter) \
              + " where product_id =" + str(product_summary.product_id) \
              + " and product_quarter=" + str(product_summary.product_quarter)
    else:
        sql = "INSERT INTO product_summary (product_id, product_year, product_quarter, product_counter)" \
              " VALUES (%s, %s, %s, %s)"

        sql = sql % (product_summary.product_id, product_summary.product_year,
                     product_summary.product_quarter, product_summary.product_counter)

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        # Rollback in case there is any error
        db.rollback()
    cursor.close()
    db.close()


def select_product_summary(product_id, quarter):
    db = connect_db()
    cursor = db.cursor()

    sql = "select * from product_summary where product_id=" + str(product_id) + " and product_quarter = " + str(quarter)

    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is not None:
            return True
        else:
            return False
    except Exception as e:
        print(e)
    cursor.close()
    db.close()


# return customer report list
def customer_report(customer_id, quarter):
    customer_report_list = []
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT a.transaction_datetime, SUM(transaction_amount), b.product_name " \
          "FROM transaction AS a, product AS b where a.product_id=b.product_id and a.customer_id="+str(customer_id) \
          + " and a.transaction_quarter in (" + str(quarter-1) + "," + str(quarter) + ") group by a.product_id"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            transaction_datetime = row[0].strftime("%Y-%m-%d")
            transaction_amount = round(row[1], 2)
            product_name = row[2]
            one_record = [transaction_datetime, transaction_amount, product_name]
            customer_report_list.append(one_record)
    except Exception as e:
        print(e)
    db.close()
    return customer_report_list



