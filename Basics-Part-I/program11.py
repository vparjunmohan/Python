'''Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number'''

def doc():
    fname = input('Enter function name: ')
    if fname in __doc__:
        print(fname.__doc__)
    else: 
        print(fname,'function dont exist')
doc()