' Write a Python program to convert all units of time into seconds.'

days = int(input('Enter number of days ')) 
hours = int(input('Enter hours ')) 
minutes = int(input('Enter minutes ')) 
seconds = int(input('Enter seconds '))

time = (days* 3600 * 24) + (hours * 3600) + (minutes * 60) + seconds

print('{}days {}hours {}minutes {}seconds'.format(days,hours,minutes,seconds),'is',time,'seconds.')