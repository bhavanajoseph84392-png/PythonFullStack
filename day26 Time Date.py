'''
Date and time
-->Python provides the built in date time module to work dates and time.....
import datetime

import datetime
today = datetime.date.today()
now = datetime.datetime.now()
print(now)
print(today)


import datetime
now = datetime.datetime.now()
print(f"Year is:{now.year}")
print(f"Month is:{now.month}")
print(f"Day is:{now.day}")
print(f"Hour is:{now.hour}")
print(f"Minute is:{now.minute}")
print(f"Second is:{now.second}")


Formatting date and time
--->strftime() is used to formate date and time

%d-->day
%m-->month
%Y-->Year
%H-->Hour
%M-->min
%S-->sec


import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H-%M-%S"))

import datetime
date_1=datetime.date(2026,6,1)
date_2=datetime.date(2026,6,15)
differ_=date_2-date_1
print(differ_)



timedelta

import datetime
today = datetime.date.today()
future_ = today + datetime.timedelta(days=7)
print(future_)

import datetime
day_ = datetime.date.today()
print(day_.weekday())


ctime:-
-->we will be getting that month name number and which day

import datetime
day_ = datetime.date.today()
print(day_.ctime())


import calendar
import datetime
today = datetime.date.today()
year = today.year
month = today.month
print(calendar.month(year,month))

import calendar
year = 2025
month =8
print(calendar.month(2025,8))

import calendar
year = 2026

print(calendar.calendar(2026))

import calendar
print(calendar.isleap(2024))

'''



import smtplib
from email.message import EmailMessage
import  time
import datetime
sender_mail = 'bhavanajoseph84392@gmail.com'
password ='ukyebbalqfvcdmbu'
target_time = '10:50'
while True:
    current_time= datetime.datetime.now().strftime('%H:%M')
    if current_time == target_time:
        eps = EmailMessage()
        eps['Subject']= 'Welcome Mail'
        eps['From']=sender
        eps['To'] = 'saranyasiri2005@gmail.com'
        eps.set_content('Hello')
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender,password)
        server.send_message(eps)
        server.quit()
        break

    time.sleep(30)






























































































