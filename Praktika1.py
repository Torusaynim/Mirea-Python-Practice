from math import *

def f11(x, y):
    a = sqrt((sin(x)+pow(x, 6))/(pow(y, 8)-35*y))
    b = sqrt((sin(x)-pow(x, 5))/(62*pow(y, 5)+22*pow(x, 8)+40))
    c = (pow(x, 5)-cos(y))/(pow(e, y)-tan(x))
    return a - b - c

def f12(x):
    if x < 145:
        return sin((x/4)-28*pow(x, 6))+pow(x, 6)/71
    else:
        if x < 197:
            return log(log(x)-pow(x, 2))-pow(x, 5)
        else:
            if x < 292:
                return pow(x, 6)-sin(x)
            else:
                return pow(x, 3)/44+abs(x)

def f13(n, m):
    a = 0
    b = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            a += pow(i, 6)+pow(i, 8)
            b += abs(j) + 12*pow(j, 2)
    return a/64-91*b

def f14(n):
    if n == 0:
        return 4
    else:
        return tan(f14(n-1))-abs(f14(n-1))