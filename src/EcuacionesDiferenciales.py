import numpy as np
import math as m

def rungeKuttaOrden4(f, y0, x0, x, d):
    xActual = x0
    yActual = y0
    while xActual < x-d:
        rk1 = f(xActual, yActual)
        rk2 = f((xActual + d / 2.0), yActual + (d * rk1 / 2.0))
        rk3 = f((xActual + d / 2.0), yActual + (d * rk2 / 2.0))
        rk4 = f((xActual + d), yActual + (d * rk3))
        yActual = yActual + ((rk1 + 2*rk2 + 2*rk3 + rk4) * d / 6)
        xActual = xActual + d
        print yActual
    return yActual

func = lambda x, y: -2*x*y
y0= 1.0
x0 = 0.0
x=1.0
d = 0.1
print rungeKuttaOrden4(func, y0, x0, x, d)