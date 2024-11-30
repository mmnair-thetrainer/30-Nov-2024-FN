#created by manu nair
import smtplib, ssl

smtp_host ="mail.mmnair.com"
sender = 'reach@mmnair.com'
receiver = 'academy@infinitiwire.com'

message = """From: M M Nair <reach@mmnair.com>
To: Academy <academy@infinitiwire.com>
Subject: Test Mail

This is a test mail
"""
context = ssl.create_default_context()
try:
    smtp_obj = smtplib.SMTP_SSL(smtp_host,465, context=context)
    password = input("Password: ")
    smtp_obj.login(sender,password)
    smtp_obj.sendmail(sender, receiver, message)
    print ("Mail sent")
except Exception:
    print("Error: Mail can't be sent")