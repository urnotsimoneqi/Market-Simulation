#!/usr/bin/python3

import pymysql
from customer import Customer
from seller import Seller
from stock import Stock


def connect_db():
    db = pymysql.connect("localhost", "root", "Simon19980908", "TESTDB")
    return db


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


# initialize sellers
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
                             transaction_quantity, transaction_amount) \
                             VALUES ('%s', %s, %s, %s, %s, %s, %s, %s)"
    sql = sql % (txn.timestamp, txn.year, txn.quarter, txn.seller_id, txn.customer_id, txn.product_id,
                 txn.quantity, txn.total_amount)
    try:
        cursor.execute(sql)
        print("Insert successfully")
        db.commit()
    except Exception as e:
        # Rollback in case there is any error
        print(e)
        db.rollback()
    db.close()


# related product
def if_related_product(product_id1, product_id2):
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT * FROM related_product where related_product_id1=" + product_id1 \
          + "and related_product_id2=" + product_id2

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if results is None:
            return False
        else:
            return True
    except Exception as e:
        print(e)
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
    most_popular_product = dict()
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
