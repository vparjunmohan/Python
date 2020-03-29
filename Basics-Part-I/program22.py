'Write a Python program to count the number 4 in a given list.'

def count():
    c = 0
    numlist = numbers.split(" ")
    for i in numlist:
        if i == '4':
            c += 1
        else:
            pass
    print('Number 4 occured',c,'times') 
    
numbers = input('Enter the numbers seperated by space ')
count()