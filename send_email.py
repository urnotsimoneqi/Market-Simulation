import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER_ROBOT = 'a0198900xrobot@gmail.com'
RECEIVER_ROBOT = 'a0198900xreceiver@gmail.com'
PASSWORD = 'A0198900X'
file = '/data/test.pdf'


def send_mail(from_addr, to_addr, filename):
    if '@gmail' in from_addr:
        if filename == 'NULL':
            send_email_no_attachment(from_addr, to_addr)
        else:
            send_email_html_attachment(from_addr, to_addr, filename)
    else:
        return 'Not support this email'


def send_email_no_attachment(from_addr, to_addr):
    sender_email = from_addr
    receiver_email = to_addr
    password = PASSWORD

    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the HTML version of your message
    subject, msg_body = customize_email()
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


def send_email_html_attachment(from_addr, to_addr, filename):
    sender_email = from_addr
    receiver_email = to_addr
    password = PASSWORD

    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the HTML version of your message
    subject, msg_body = customize_email()
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


def customize_email():
    """draft different email subject and content based on different query type

    Args:
        data: a list of analyzed data
        type: query type, including 'BUY', 'SELL', 'REPORT', 'INV_FORMAT'

    Return: return the subject of mail and body of mail
    """
    subject = "FOR TEST"
    msg_body = "FOR TEST"

    return subject, msg_body


send_mail(SENDER_ROBOT, 'A0198890Hrobot@gmail.com', "NULL")