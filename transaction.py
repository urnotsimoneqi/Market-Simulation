import time


class Transaction:
    # Define the status of a Transaction
    SUCCESS_STATUS = 1
    FAILED_STATUS = -1
    CANCELED_STATUS = 2

    def __init__(self, timestamp, seller_id, customer_id, product_id, quantity, total_amount):
        # self.id = id
        self.timestamp = timestamp
        self.seller_id = seller_id
        self.customer_id = customer_id

        self.product_id = product_id
        self.quantity = quantity
        self.total_amount = total_amount

        self.timestamp = timestamp
        # self.status = status
        # self.year = timestamp.
        # self.quarter =
