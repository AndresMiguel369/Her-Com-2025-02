import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import quad

def func1(x):
    return x**2

def func2(x):
    return 1/np.sqrt(np.exp(-x) + np.sqrt(x) + 2*x)

def func1_integral(a,b):
    return (1/3)*(b**3 - a**3)

def gaussiana(x):
    return np.exp(-x**2)

def Monte_Carlo(func, a, b , N):
    vals = np.random.uniform(a, b, N)
    y = func(vals)
    y_prom = np.mean(y)
    integral = (b-a)*y_prom
    return integral

print(f'Integral: {func1_integral(-2,2):.10f}')
print(f'Monte Carlo: {Monte_Carlo(func1,-2,2,50000):.10f}')

x = np.linspace(-4, 4, 500)
plt.figure(figsize = (7,5))
plt.plot(x, gaussiana(x), color = 'red', label = 'f(x)')
plt.fill_between(x, gaussiana(x), color = 'red', alpha = 0.2)
print(f'Monte Carlo de la gausiana: {Monte_Carlo(gaussiana,-10,10,100000):.10f}')
print(f'Pi por integral monte carlo: {Monte_Carlo(gaussiana,-10,10,100000)**2:.10f}')
print(f'Pi teorico: {np.pi:.10f}')
plt.show()

plt.figure(figsize = (7,5))
integral1,error = scipy.integrate.quad(func2, 0, 10)

x = np.linspace(0,10,100)

plt.plot(x, func2(x), color = 'red', label = 'f(x)')
plt.fill_between(x, func2(x), color = 'red', alpha = 0.2)
print(f'Integral: {Monte_Carlo(func2, 0, 10, 100000):.10f}')
print(f'Valor teorico: {integral1:.10f}')
plt.show()