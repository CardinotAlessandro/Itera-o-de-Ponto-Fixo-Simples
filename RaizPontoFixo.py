import matplotlib.pyplot as plt
import numpy as np

W = 10**6
V = 10**6
Q = 10**5
k = 0.25

def F(c):
    return W - Q*c - c**0.5*k*V

def G(c):
    return ((W - (c**0.5*k*V))/Q) 

def ponto_fixo(c0, tol, n):
    ci = c0
    err = 1
    cip1 = 0
    ct = 0
    while err > tol and ct < n:
        cip1 = G(ci)
        err = abs(((cip1 - ci) / cip1) * 100)
        print(f"ci = {ci}, ci+1 = {cip1}, f(ci) = {F(ci)}, err = {err}")
        ci = cip1
        ct += 1
        

ponto_fixo(1, 0.0000001, 100)

c = np.arange(4, 6, 1)
y = np.arange(-100000, 100000, 1)

plt.plot(c, F(c), linewidth = 2.0)
plt.plot(c, c*0, "black", linewidth = 1.0)
plt.plot(y*0 + 4, y, "black", linewidth = 1.0)

plt.show()
