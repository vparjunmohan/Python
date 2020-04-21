'Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount.'


def no_notes(a):
    Q = [500, 200, 100, 50, 20, 10, 5]
    x = 0
    for i in range(7):
        q = Q[i]
        x += int(a / q)
        a = int(a % q)
    if a > 0:
        x = -1
    return x


print(no_notes(885))
print(no_notes(1000))
