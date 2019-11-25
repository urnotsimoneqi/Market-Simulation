import mysql
import send_email


def send_customer_email(customer_id, SENDER_ROBOT, customer_email, seller_performance):
    customer_report_list = mysql.customer_report(customer_id, quarter=4)
    send_email.send_email_no_attachment(SENDER_ROBOT, customer_email, customer_report_list, seller_performance)

def send_seller_email(seller_name, SENDER_ROBOT, RECEIVER_ROBOT , file_path):
    send_email.send_email_html_attachment(SENDER_ROBOT, RECEIVER_ROBOT, seller_name, file_path)
