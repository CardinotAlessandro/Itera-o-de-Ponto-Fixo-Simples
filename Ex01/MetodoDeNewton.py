import matplotlib.pyplot as plt
import numpy as np


V = 10**6
Q = 10**5
W = 10**6
k = 0.25

def f(c):
    return W - Q * c - k*V*(c**0.5)

def df(c):
    return -Q - (k*V)/(2*c**0.5)

def d2f(c):
    return 0.74*(k*V)/c**1.5

def Newton(x, tol, n):
    xi = x
    err = 1
    c = 0
    while err > tol and c < n:
        xip1 = xi - f(xi)/df(xi)
        err = (-d2f(xip1)/(2*df(xip1)))*err**2
        print(f"xi+1 = {xip1}, xi = {xi}, f(x1p1) = {f(xip1)}, err = {err}")
        xi = xip1
        c += 1

Newton(1, 10**-4, 100)
