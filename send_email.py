import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER_ROBOT = 'a0198900xrobot@gmail.com'
RECEIVER_ROBOT = 'a0198900xreceiver@gmail.com'
PASSWORD = 'A0198900X'

def send_mail(from_addr, to_addr, data, filename):
    if '@gmail' in from_addr:
        if filename == 'NULL':
            send_email_no_attachment(from_addr, to_addr, data)
        else:
            send_email_html_attachment(from_addr, to_addr, data, filename)
    else:
        return 'Not support this email'


def send_email_no_attachment(from_addr, to_addr, data, seller_performance):
    sender_email = from_addr
    receiver_email = to_addr
    password = PASSWORD

    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the HTML version of your message
    subject, msg_body = customize_email(data, seller_performance)
    message["Subject"] = subject

    # Turn these into plain/html MIMEText objects
    part = MIMEText(msg_body, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def send_email_html_attachment(from_addr, to_addr, data, filename):
    sender_email = from_addr
    receiver_email = to_addr
    password = PASSWORD

    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the HTML version of your message
    subject, msg_body = customize_seller_email(data)
    message["Subject"] = subject

    # Turn these into plain/html MIMEText objects
    part = MIMEText(msg_body, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part)

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, text
        )


def customize_email(data, seller_performance):
    subject = ""
    msg_body = ""
    # msg_to_seller = """
    #     <h2><strong>Sales Analysis Summary Report</strong></h2>
    #     <hr />
    #     <p>Dear """ + seller.name + """</p >
    #     <p>We're consolidate a <strong>summary report</strong> as attached for your information to make better business decisions.&nbsp;</p >
    #     <p>We hope this will help you. Looking forward to your future performance in the market.</p >
    #     <p>Sincerely,</p >
    #     <div>Group 9</div>
    #     <div><span style="text-decoration: line-through;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></div>
    #     <div>Intelligent System Deployment Research Lab</div>
    #     <div>13 Computing Drive,&nbsp;117417</div>
    #     <div>Tel:6516 6666</div>
    #     <div>A0198890Hrobot@gmail.com</div>
    # """

    top_3_sellers = "<ol>"
    for sales in seller_performance:
        top_3_sellers += "<li>" + str(sales[0]) + "</li>"
    top_3_sellers += "</ol>"

    if data is None or len(data) == 0:
        subject = "We Miss You"
        msg_body = """
        
        <p>Dear Valued Customer,</p >
        <p>It&rsquo;s been a while since we last saw you at the club, and we miss you.</p >
        <p>We are glad to share with you the <strong>Top 3 Sellers</strong> according to our latest stats, you may want to check out.</p >
        """ + top_3_sellers + """
        <p>For assistance at any time, please call us at 0000-123 4567 (or +65 6516 6666 from overseas). Alternatively, you can email us at <a href=" "> a0191561e.robot@gmail.com </a ></p >
        <p>Thank you for working with us. We look forward to helping you purchase online.</p >
        <p>Sincerely,</p >
        <div>Group 9</div>
        <div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</div>
        <div>Your Purchase Advisor</div>
        <div>13 Computing Drive,&nbsp;117417</div>
        <div>Tel:6516 6666</div>
        <div>a0191561e.robot@gmail.com</div>
        """
    elif data is not None and len(data) > 0:
        customer_records = "<ul>"
        for record in data:
            customer_records += "<li>" + str(record[2]) + "  " + str(record[1]) + "   " + str(record[0]) + "</li>"
        customer_records += "</ul>"

        subject = "Your Purchasing Summary"
        msg_body = """
            <p>Dear Valued Customer</p >
            <p>Thank you for using our system when making your online purchase.&nbsp;</p >
            <p>We're glad to generate <strong>a summary report for your purchasing records</strong> in previous quarter:&nbsp;</p >
            """ + customer_records + """
            <p>&nbsp;</p >
            <p>We are glad to share with you the<strong> Top 3 Sellers</strong> according to our latest stats:</p >
            """ + top_3_sellers + """
            <p>&nbsp;</p >
            <p>For assistance at any time, please call us at 0000-123 4567 (or +65 6516 6666 from overseas). Alternatively, you can email us at <a href=" ">a0191561e.robot@gmail.com</a ></p >
            <p>Thank you for working with us. We look forward to helping you purchase online.</p >
            <p>Sincerely,</p >
            <div>Group 9</div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</div>
            <div>Your Purchase Advisor</div>
            <div>13 Computing Drive,&nbsp;117417</div>
            <div>Tel:6516 6666</div>
            <div>a0191561e.robot@gmail.com</div>
            """
        pass

    return subject, msg_body


def customize_seller_email(name):
    subject = "Sales and Profit Analysis Result"
    msg_body = """
            <html>
                <body>
                <h2><strong>Sales and Profit Analysis Result</strong></h2>
                <hr />
                <p>Dear """ + str(name) + """,</p >
                <p>We're consolidate a <strong>summary report</strong> as attached for your information to make better business decisions.&nbsp;</p >
                <p>We hope this will help you. Looking forward to your future performance in the market.</p >
                <p>Sincerely,</p >
                <div>Group 9</div>
                <div><span style="text-decoration: line-through;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></div>
                <div>Intelligent System Deployment Research Lab</div>
                <div>13 Computing Drive,&nbsp;117417</div>
                <div>Tel:6516 6666</div>
                <div>A0198890Hrobot@gmail.com</div>
                </body>
            </html>
            """

    return subject, msg_body