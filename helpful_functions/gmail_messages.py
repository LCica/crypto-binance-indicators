import smtplib, ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_gmail = "Type In Sender Gmail"  
receiver_gmail = "Type In Receiver Gmail"
password = "Type In Password"
context = ssl.create_default_context()

def sell_message(price):
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:    
        message1 = """\
        Subject: Binance message

        You sold for: {} EUR""".format(price)           
        server.login(sender_gmail, password)
        server.sendmail(sender_gmail, receiver_gmail, message1)
def buy_message(price):
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:    
        message2 = """\
        Subject: Binance message

        You bought for: {} EUR""".format(price)
        server.login(sender_gmail, password)
        server.sendmail(sender_gmail, receiver_gmail, message2)
def percentage(proc,buy,sell):
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:    
        message2 = """\
        Subject: Binance message

        Your buy was at {} EUR,
        Your sell was at {} EUR,
        Your percentage profit/loss is: {} %""".format(buy,sell,proc)
        server.login(sender_gmail, password)
        server.sendmail(sender_gmail, receiver_gmail, message2)

def error():
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:    
        message2 = """\
        Subject: Binance message

        There was an error!!"""
        server.login(sender_gmail, password)
        server.sendmail(sender_gmail, receiver_gmail, message2)