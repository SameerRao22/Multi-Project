import math
from fractions import Fraction

def f(x,y):
    return x+y

def t(x,y,h,b,vals):
    s = 0
    k = []
    for i in range(len(b)):
        xn = x + vals[i][0]*h
        yn = y
        if i != 0:
            a = vals[i][1]
            for j in range(i-1):
                yn += h*a[j]*k[j]
        k.append(f(xn, yn))
        s += f(xn, yn)*b[i]
    return h*s

def approx(x0, y0, xf, s, b, vals):
    x = x0
    y = y0
    h = (xf-x0)/float(s)
    for i in range(s):
        y += t(x, y, h, b, vals) 
        x += h
        p = (x, y)
    return x, y

def tableau(name):
    with open(name, "r") as f:
        raw = f.readlines()
        raw_vals = raw[:len(raw)-1]
        b = [float(Fraction(x)) for x in raw[-1].split()]
        vals = []
        for i in raw_vals:
            j = i.split()
            c = float(Fraction(j[0]))
            a = [float(Fraction(x)) for x in j[1:]]
            vals.append((c, a))
    s = sum(b)
    flag = (s>=0.99) and (s <= 1.0) and (len(b) == len(vals))
    return b, vals, flag


if __name__ == '__main__':
    b, vals, flag = tableau('tableaus/rk4.txt')
    if not flag:
        print('invalid tableau')
    else:
        print(approx(1,1,2,100,b,vals))

    b, vals, flag = tableau('tableaus/euler.txt')
    if not flag:
        print('invalid tableau')
    else:
        print(approx(1,1,2,100,b,vals))
