# from smtplib import SMTP
import smtplib
import os

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
password = #where you have to put your password
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()  # identifies ourselves with the mail server
    smtp.starttls()  # encrypt the traffic
    smtp.ehlo()
    smtp.login('kenadamsfriends100@gmail.com', password)

    subject = "Hi , This is test email?"
    body = 'I sent this email using python script'

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail('kenadamsfriends100@gmail.com','receiver email add', msg)
