'Write a Python program to test whether a number is within 100 of 1000 or 2000.'

def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
n = int(input('Enter a number '))
print(near_thousand(n))
