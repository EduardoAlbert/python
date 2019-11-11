import datetime

now = datetime.datetime.now()

# CREATE TIME
""" 
t = datetime.time(7, 21, 43)

print(t) """

""" today = datetime.date.today()

print(today) """

# DIFFERENCE BETWEEN TWO DATES

d1 = datetime.date(2001, 6, 5)

d2 = d1.replace(year=2019)

print(d2 - d1)

