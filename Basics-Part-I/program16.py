" Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference."

num = int(input('Enter a number '))

if num < 17:
    diff = 17 - num
    print(diff)
else:
    diff =  (abs(num-17)) * 2
    print(diff) 
