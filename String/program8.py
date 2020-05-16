'Write a Python function that takes a list of words and returns the length of the longest one.'


def wordlength(lwords):
    wordlist = lwords.split(',')
    for i in wordlist:
        print('Length of {} is {}'.format(i, len(i)))


lwords = input('Enter list of words seperated by commas: ')
wordlength(lwords)
