import smtplib, ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "type in sender_email"  
receiver_email = "type in receiver_email"  
password = "type in password"
context = ssl.create_default_context()

def sell_message(price):
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:    
        message1 = """\
        Subject: Binance message

        You sold for: {} EUR""".format(price)           
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message1)
def buy_message(price):
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:    
        message2 = """\
        Subject: Binance message

        You bought for: {} EUR""".format(price)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message2)