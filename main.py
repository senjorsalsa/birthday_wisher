import smtplib
import datetime as dt
import pandas
import os

APP_PW = "ENVIRONMENT_VAR"
df = pandas.read_csv("birthdays.csv")
all_persons = df.to_dict(orient="records")
now = dt.datetime.now()
current_day = now.day
current_month = now.month
my_email = "victorpythontest@gmail.com"

for person in all_persons:
    if current_day == person["day"] and current_month == person["month"]:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=APP_PW)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!\n\nMessage fetched from files")
