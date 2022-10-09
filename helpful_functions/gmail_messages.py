import smtplib, ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "kojikurac2k1@gmail.com"  
receiver_email = "kojikurac2k1+binance@gmail.com"  
password = "fitlrgcrbmlrkpxu"
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
def percentage(proc,buy,sell):
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:    
        message2 = """\
        Subject: Binance message

        Your buy was at {} EUR,
        Your sell was at {} EUR,
        Your percentage profit/loss is: {} %""".format(buy,sell,proc)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message2)
