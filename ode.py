import math

'''
tan(y) + 1
'''

def f(x,y):
    return math.tan(y) + 1


'''
T4 = 1/6 (k1 + 2k2 + 2k3 + k4)
k1 = f(x,y)
k2 = f(x + h/2, y + h/2*k1)
k3 = f(x + h/2, y + h/2*k2)
k4 = f(x + h, y + h*k3)
'''

def t(x,y,h): 
    k1 = f(x,y)
    k2 = f(x + h/2, y + h/2*k1)
    k3 = f(x + h/2, y + h/2*k2)
    k4 = f(x + h, y + h*k3)
    return 1/6 * (k1 + 2*k2 + 2*k3 + k4)


'''
y1 = y0 + h*T4(x,y,h)
'''

def approx(x, y, h):
    return h*t(x,y,h)

def rk4(x0, y0, h, s):
    x = x0
    y = y0
    for i in range(s):
        y += approx(x, y, h) 
        x += h
        p = (x, y)
        print(p)
    return x, y

if __name__ == '__main__':
    rk4(1, 1, 0.0250, 4)
