import math
from fractions import Fraction
import matplotlib.pyplot as plt

def f(x,y):
    return x*y

def o(x):
    return math.pow(math.e, math.pow(x,2)/2)

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
    p = []
    for i in range(s):
        y += t(x, y, h, b, vals) 
        x += h
        p.append((x, y))
    return p

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
        p1 = approx(0,1,1,100,b,vals)

    b, vals, flag = tableau('tableaus/euler.txt')
    if not flag:
        print('invalid tableau')
    else:
        p2 = approx(0,1,1,100,b,vals)

    h = (1)/float(100)
    px = [i[0] for i in p1]
    py = [j[1] for j in p1]


    y = [o(g) for g in px]

    plt.plot(px, py, label = 'approx.')
    plt.plot(px, y, label = 'legit')

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Bench press mark')
    plt.legend()
    plt.show()
