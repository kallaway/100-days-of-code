import datetime as dt
import pandas as pd
import random
import smtplib
##################### Normal Starting Project ######################
MY_EMAIL = "christianwebdeveloper57@gmail.com"
MY_PASSWORD = "5nH1O%Cj4nA1%h"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthdays = pd.read_csv("birthdays.csv")

birthdays_dict = {(birthdays_row.month, birthdays_row.day): birthdays_row for (index, birthdays_row) in birthdays.iterrows()}
# or {(birthdays["month"], birthdays["day"]): birthdays_row for (index, birthdays_row) in birthdays.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

