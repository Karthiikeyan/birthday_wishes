import smtplib
import pandas
from datetime import datetime
import random
import ssl
from email.message import EmailMessage

mail = EmailMessage()

my_mail = 'YOUR EMAIL'
my_password = 'YOUR EMAIL PASSWORD'
receiver = 'RECEIVER EMAIL'
subject = "Happy Birthday"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row  for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    file_path = f"letter_templates\letter_{random.randint(1,3)}.txt"
    birthday_data = birthday_dict[today_tuple]

    with open(file_path) as letter:
        content = letter.read()
        contents = content.replace("[NAME]",birthday_data["name"])

    mail['From'] = my_mail
    mail['To'] = receiver
    mail['subject'] = subject
    mail.set_content(contents)

    contaxt = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contaxt) as connection:
        connection.login(my_mail, my_password)
        connection.sendmail(from_addr=my_mail, to_addrs=receiver, msg=mail.as_string())



