import smtplib
import datetime as dt
import random

MY_EMAIL = "christianwebdeveloper57@gmail.com"
MY_PASSWORD = "5nH1O%Cj4nA1%h"
SEND_EMAIL = "billhall105@yahoo.com"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=SEND_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
