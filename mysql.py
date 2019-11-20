#!/usr/bin/python3

import pymysql
from customer import Customer
import json

def register_customer():
    customers = []
    db = pymysql.connect("localhost", "root", "Simon19980908", "TESTDB")
    cursor = db.cursor()
    sql = "SELECT * FROM customer"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            userId = row[0]
            name = row[1]
            wallet = row[2]
            tolerance = row[3]
            customer = Customer(name=name, wallet=wallet, tolerance=tolerance)
            customers.append(customer)
    except:
        print("Error: unable to fetch data")
    db.close()
    print(customers)
    return customers
