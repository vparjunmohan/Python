'Write a Python program to count the number occurrence of a specific character in a string.'

def charcount():
    count = 0
    for i in string:
        if i == char:
            count += 1
        else:
            pass
    print('Total count of {} in {} is {}'.format(char,string,count))

string = input('Enter a string: ')
char = input('Enter the character to be counted in the string: ')

charcount()