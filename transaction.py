import time


class Transaction:
    # Define the status of a Transaction
    SUCCESS_STATUS = 1
    FAILED_STATUS = -1
    CANCELED_STATUS = 2

    def __init__(self, datetime, seller_id, customer_id, product_id, quantity, total_amount, related_product_id=0,
                 promotion_id="", status=""):
        # self.id = id
        self.datetime = datetime
        self.timestamp = datetime.strftime("%Y-%m-%d %H:%M:%S")
        self.year = datetime.year
        self.quarter = (datetime.month - 1) // 3 + 1

        self.seller_id = seller_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_amount = total_amount

        self.related_product_id = related_product_id
        self.promotion_id = promotion_id
        self.status = status