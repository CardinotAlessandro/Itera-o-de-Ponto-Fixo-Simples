import matplotlib.pyplot as plt
import numpy as np

V = 10**6
Q = 10**5
W = 10**6
k = 0.25

def f(c):
    return W - Q*c - k*V*(c**0.5)

def Media(a, b):
    return (a+b)/2

def Bissecao(e, d, tol, n):
    xu = e
    xl = d
    xr = Media(xu, xl)
    err = 1
    k = 0
    while err > tol and k < n:
        if(f(xu) * f(xr) < 0):
            xl = xr
        elif(f(xl) * f(xr) < 0):
            xu = xr
        else:
            print("Não foi encontrado nenhuma raiz nesse intervalo.\n")
            break
        
        xrn = Media(xu, xl)
        err = abs((xrn - xr)/xrn)
        print(f"xu = {xu}, xl = {xl}, xr = {xr}, err = {err:.10f}")
        xr = xrn
        k += 1

Bissecao(0, 100, 10**-4, 100)

            

