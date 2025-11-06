import numpy as np
import scipy
from scipy.integrate import quad

D = 3
n = 10000
Z = (D/2) +1
A = (4/3)*np.pi
ext = 15

def funcgamma(t, z = Z):
    return (t**(z-1))*(np.exp(-t))

def Mc_integral(func, a, b , N):
    vals = np.random.uniform(a, b, N)
    y = func(vals)
    y_prom = np.mean(y)
    integral = (b-a)*y_prom
    return integral

integral1,error = scipy.integrate.quad(funcgamma, 0, ext)

n_e = 0
for i in range(n):
    x1 = np.random.uniform(0, 1, D)
    Rsq = 0
    for j in range(D):
        Rsq += x1[j]**2
    R = np.sqrt(Rsq)
    if R <= 1:
        n_e += 1


Vol_mcg = np.pi**(D/2) / Mc_integral(funcgamma, 0.00001, ext, 10000000)
Vol_scipy = np.pi**(D/2) / integral1
Vol_m = (n_e/n)*(2**D)


print(f'Solucion Monte Carlo:           {Vol_m:.12f} r^{D}')
print(f'Solucion Monte Carlo con gamma: {Vol_mcg:.12f} r^{D}')
print(f'Solucion analitica:             {A:.12f} r^{D}')
print(f'Solucion por Scipy con gama:    {Vol_scipy:.12f} r^{D}')