'''Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. Go to the editor
Test Data : amt = 10000, interest = 3.5, years = 7
Expected Output : 12722.79'''

def futureValue():
    return amt*((1+(0.01*interest)) ** years)

amt =  int(input('Enter amount '))
interest =  float(input('Enter interest '))
years =  int(input('Enter years '))

print('Future value is',futureValue())