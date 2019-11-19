import time


class Transaction:
    # Define the status of a Transaction
    SUCCESS_STATUS = 1
    FAILED_STATUS = -1
    CANCELED_STATUS = 2

    def __init__(self, id, product_id, quantity, total_amount, seller_id, buyer_id, timestamp, status):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.total_amount = total_amount
        self.seller_id = seller_id
        self.buyer_id = buyer_id
        self.timestamp = timestamp
        self.status = status
