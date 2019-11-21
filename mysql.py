#!/usr/bin/python3

import pymysql
from customer import Customer
from product import Product
from seller import Seller
from stock import Stock


def connect_db():
    print('Connecting to Mysql Server...')
    db = pymysql.connect("localhost", "root", "Simon19980908", "TESTDB")
    print('Connect Successfully!')
    return db


def initialize_customer():
    customers = []
    # db = pymysql.connect("localhost", "root", "Simon19980908", "TESTDB")
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
            customer = Customer(name=customer_name, wallet=customer_wallet, tolerance=customer_tolerance)
            customers.append(customer)
    except:
        print("Error: unable to fetch customer")
    db.close()
    return customers


# initialize certain seller's stock
def initialize_stock(seller_id):
    stock_list = []
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT a.product_id, a.product_name, a.product_quality, a.product_status, " \
          "b.seller_id, b.stock_quantity, b.stock_cost, b.stock_price FROM " \
          "product AS a,stock AS b where a.product_id=b.product_id and b.seller_id= " + str(seller_id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            product_id = row[0]
            product_name = row[1]
            product_quality = row[2]
            product_status = row[3]
            seller_id = row[4]
            stock_quantity = row[5]
            stock_cost = row[6]
            stock_price = row[7]
            stock = Stock(product_id=product_id, product_name=product_name, product_quality=product_quality,
                          product_status=product_status, seller_id=seller_id, stock_quantity=stock_quantity,
                          stock_cost=stock_cost, stock_price=stock_price)
            stock_list.append(stock)
    except:
        print("Error: unable to fetch stock")
    db.close()
    return stock_list

# initialize certain seller's products
def initialize_product(seller_id):
    products = []
    # db = pymysql.connect("localhost", "root", "Simon19980908", "TESTDB")
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT a.product_id, a.product_name, a.product_quality, a.product_status, b.stock_price, b.stock_quantity FROM " \
          "product AS a,stock AS b where a.product_id=b.product_id and b.seller_id= " + str(seller_id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            product_id = row[0]
            product_name = row[1]
            product_quality = row[2]
            product_status = row[3]
            product_price = row[4]
            product_quantity = row[5]
            product = Product(product_id=product_id, name=product_name, price=product_price,
                              quality=product_quality, quantity=product_quantity)
            products.append(product)
    except:
        print("Error: unable to fetch product")
    db.close()
    return products


# initialize sellers
def initialize_seller():
    sellers = []
    # db = pymysql.connect("localhost", "root", "Simon19980908", "TESTDB")
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
            # seller_products = initialize_product(seller_id)
            seller_products = initialize_stock(seller_id)
            seller = Seller(name=seller_name, products=seller_products, wallet=seller_wallet)
            sellers.append(seller)
    except:
        print("Error: unable to fetch seller")
    db.close()
    return sellers


def reporting(revenue, expenses, profit):
    db = connect_db()
    # db = pymysql.connect("localhost", "root", "Simon19980908", "TESTDB")

    db.close()
