import numpy as np
d = 1.0
L = 1.0
N = 500000

x0    = np.random.uniform(0,d/2,N)       # Número de distancias al interlineado
theta = np.random.uniform(0,np.pi/2,N)   # Número de orientaciones
corte = x0 < ((L/2)*np.sin(theta))         # Aquí se detecta el corte

C = np.cumsum(corte)                     # Suma de los cortes
piEst = 2*L*N/(d*C)
errAbs = np.abs(np.pi - piEst)
print(f"pi = {np.pi}")
print(f"pi estimado = {piEst[-1]}")
