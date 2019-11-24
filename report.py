import mysql


def send_customer_email(customer_id):
    customer_report_list = mysql.customer_report(customer_id, quarter=4)
    return customer_report_list

print(send_customer_email(4))
