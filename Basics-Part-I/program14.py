'''Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''

import datetime

f_date = input('Enter first date in YYYY-MM-DD format ')
year,month,date = map(int, f_date.split('-'))
date1 = datetime.date(year, month, date)
#print(date1)

l_date = input('Enter last date in YYYY-MM-DD format ')
year,month,date = map(int, l_date.split('-'))
date2 = datetime.date(year, month, date)
#print(date2)

print('The difference between',date1,'and',date2,'is',(date2 - date1).days,'days')
