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


def send_email_no_attachment(from_addr, to_addr, data):
    sender_email = from_addr
    receiver_email = to_addr
    password = PASSWORD

    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the HTML version of your message
    subject, msg_body = customize_email(data)
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
    subject, msg_body = customize_email(data)
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


def customize_email(data):
    """draft different email subject and content based on different query type

    Args:
        data: a list of analyzed data
        type: query type, including 'BUY', 'SELL', 'REPORT', 'INV_FORMAT'

    Return: return the subject of mail and body of mail
    """
    subject = ""
    msg_body = ""

    if data is None or len(data) == 0:
        subject = "Invalid seller data"
        msg_body = """
                 <html>
                        <style>
                            table {border-collapse: collapse;}
                            table, td, th {border: 1px solid black; padding: 5px;}
                        </style>
                        <body>
                                Dear Valued Customer<p>
                                We're sorry to inform that there's something wrong with the market.</p>
                                <p>For assistance at any time, please call us at 0000-123 4567 (or +65 1234 5678 from overseas). Alternatively, you can email us at <a href="mailto:a0191561e.robot@gmail.com">a0191561e.robot@gmail.com</a>.</p>
                                <p>Thank you for your cooperation.</p>
                                <p>Yours sincerely</p>
                                Group 9
                                <br>Your Shopping Advisor 
                                <br>IS5006
                                <br>SOC
                        </body>
                    </html>
                """
    elif data is not None:
        if len(data) >= 3:
            top_3 = data[0][0] + ', ' + data[1][0] + ', ' + data[2][0]
        elif len(data) >= 2:
            top_3 = data[0][0] + ', ' + data[1][0]
        else:
            top_3 = data[0][0]
        subject = "Investment Advisory | Together we can find an answer"
        msg_body = """
            <html>
                <body>
                       Dear Valued Customer<p>
                       Thank you for sharing your inquiry with us when making big investment decisions.</p>
                       <p>After understanding your personal investment objective and applying our intellectual capital, <b>Company """ + top_3 + """</b> would be highly recommended as your best possible investment. </p>
                       <p>For assistance at any time, please call us at 0000-123 4567 (or +65 1234 5678 from overseas). Alternatively, you can email us at <a href = "mailto: a0191561e.robot@gmail.com">a0191561e.robot@gmail.com</a>.</p>
                       <p>Thank you for working with us. We look forward to helping you deliver superior investment outcomes again in changing markets.</p>
                       <p>Yours sincerely</p>
                       Group 9
                       <br>Your Investment Advisor 
                       <br>IS5006
                       <br>SOC
                </body>
            </html>
            """
        pass

    return subject, msg_body


# send_mail(SENDER_ROBOT, RECEIVER_ROBOT, data, file)