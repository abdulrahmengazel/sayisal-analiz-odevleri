#fönksiyon kısmı  f(x) = 4*e^(- x / 2)-x:
import math


def f(x):
    return 4*math.exp(-x/2)-x

def f_birinci_Turev(x):
    return -2*math.exp(-x/2)-1

def newton_raphson(x0,  max_iter):
    i = 1
    while i <= max_iter:
        x1 = x0 - f(x0)/f_birinci_Turev(x0)
        print( f"{i} . iterasyon: {x1:.12f}")
        x0 = x1
        i += 1
