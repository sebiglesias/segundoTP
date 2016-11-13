# coding=utf-8
# Ejercicio 1
import numpy as np
import math as m
# Trapecios
# f: funcion y n: cantidad de divisiones

def trapecios(f, min, max, mDivs):
    #en caso de que entre algo no valido
    # if min>= max or mDivs<1: raise ValueError("no son válidas las entradas")
    delta = (max - min) / float(mDivs)
    resultado = 0.0
    resultado += f(min) / 2.0
    for i in range(1, mDivs):
        resultado += f(min + i * delta)
    resultado += f(max) / 2.0
    return resultado * delta


# Romberg

def romberg(f, min, max, cotaError):
    R = [[0.5 * (max - min) * (f(min) + f(max))]]  # R[0][0]
    print "Iteracion #",0
    print ' --'.join('%11.8f' % x for x in R[0])
    i = 1
    while True:
        print "Iteracion #", i
        h = float(max - min) / 2 ** i
        R.append((i + 1) * [0])
        R[i][0] = 0.5 * R[i - 1][0] + h * sum(
            f(min + (2 * k - 1) * h) for k in range(1, 2 ** (i - 1) + 1))
        for m in range(1, i + 1):
            R[i][m] = R[i][m - 1] + (R[i][m - 1] - R[i - 1][m - 1]) / (4 ** m - 1)
        print ' --'.join('%11.8f' % x for x in R[i])
        if abs(R[i][i - 1] - R[i][i]) < cotaError:
            return R[i][i]
        i += 1

def print_row(lst):
    print

# Integrales

# funciones
f1= lambda x: m.sin(x)/x
f2= lambda x: m.log(x,m.e)

for i in range(1,11):
    print "m: ",i,"mi valor", trapecios(f1,2,3,i)

romberg(f1,2,3,0.0000000001)
romberg(f2,2,3,0.0000000001)