# Ejercicio 1
import numpy as np
import math as m
# Trapecios
# f: funcion y n: cantidad de divisiones

def trapecios(f, min, max, mDivs):
    delta = (max - min) / float(mDivs)
    s = 0.0
    s += f(min) / 2.0
    for i in range(1, mDivs):
        s += f(min + i * delta)
    s += f(max) / 2.0
    return s * delta

# Romberg

def romberg(f, min, max, filas):
    I = np.zeros((filas, filas))
    for k in range(0, filas):
        # buscar la diferencia entre el valor obtenido en la iteracion n y la n-1, y definir la condicion de corte del loop
        # richardson usando trapecios
        I[k, 0] = trapecios(f, min, max, 2 ** k)
        # aca aplico efectivamente romberg
        for j in range(0, k):
            I[k, j + 1] = (4 ** (j + 1) * I[k, j] - I[k - 1, j]) / (4 ** (j + 1) - 1)
        print(I[k, 0:k + 1])
    return I

# Integrales

# funciones
f1= lambda x: m.sin(x)/x
f2= lambda x: m.log(x,m.e)

# for i in range(1,11):
#     print "m: ",i," valor trapecios", trapecios(f1,2,3,i)
#
# for i in range(1, 11):
#     print trapecios(f2, 2, 3, i)
print romberg(f1,2,3,5)
