import numpy as np
import matplotlib.pyplot as plt
import random
import scipy
from scipy.integrate import quad

Z = 7/2
A = (15/8)*np.pi**(1/2)
ext = 15

def funcgamma(t, z = Z):
    return (t**(z-1))*(np.exp(-t))

def Mc_integral(func, a, b , N):
    vals = np.random.uniform(a, b, N)
    y = func(vals)
    y_prom = np.mean(y)
    integral = (b-a)*y_prom
    return integral

x = np.linspace(0.001, ext, 100)
integral1,error = scipy.integrate.quad(funcgamma, 0, ext)

plt.figure(figsize = (4, 3))
plt.plot(x, funcgamma(x, Z), 'b')
plt.fill_between(x, funcgamma(x, Z), color = 'blue', alpha = 0.6)
print(f'Solucion Monte Carlo: {Mc_integral(funcgamma, 0.00001, ext, 10000000):.12f}')
print(f'Solucion analitica: {A:.12f}')
print(f'Solucion por Scipy: {integral1:.12f}')
plt.show()
