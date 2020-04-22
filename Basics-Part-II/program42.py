'''Write a Python program to test whether two lines PQ and RS are parallel. The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4). 
Input:
x1,y1,x2,y2,x3,y3,xp,yp separated by a single space
Input x1,y1,x2,y2,x3,y3,xp,yp:
2 5 6 4 8 3 9 7
PQ and RS are not parallel'''

print('Input x1,y1,x2,y2,x3,y3,xp,yp:')
x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
print('PQ and RS are parallel.' if abs((x2 - x1)*(y4 - y3) -
                                       (x4 - x3)*(y2 - y1)) < 1e-10 else 'PQ and RS are not parallel')
