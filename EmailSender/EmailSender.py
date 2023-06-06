from email.message import EmailMessage
from AppPassword import password
import ssl
import smtplib


email_sender = "thenekros5513@gmail.com"
email_password = password

email_receiver = "favek71305@syinxun.com"

subject = "Don't forget to take out the trash"
body = """
    The trash is full, make sure you take it out.
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
