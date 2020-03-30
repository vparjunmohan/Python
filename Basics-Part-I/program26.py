'Write a Python program to create a histogram from a given list of integers.'

def histogram():
    histList = hist.split(" ")
    for i in histList:
        output = ''
        times = int(i)
        while(times>0):
            output += '*'
            times = times -1
        print(output)

hist = input('Enter numbers separated by space ')
histogram()