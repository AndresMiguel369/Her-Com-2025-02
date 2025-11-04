import numpy as np
import matplotlib.pyplot as plt
import time

#Parametros

Nrandom = 10000
a = 0.5
b = 0.25
nAdentro = 0
N = 1000

#crear elipse

angle = np.linspace(0, 2*np.pi, 100)
x = a*np.cos(angle) + 0.5
y = b*np.sin(angle) + 0.5

t0 = time.time()
for _ in range(Nrandom):
    x = np.random.rand()
    y = np.random.rand()
    if(((x-0.5)**2)/(a**2) + ((y-0.5)**2)/(b**2) < 1):
        nAdentro += 1
        plt.plot(x, y, marker = '.', markersize = 0.5, color = 'r')

#figura

plt.figure(1)
plt. grid(True)
plt.plot(x, y, color = 'r', linestyle = '-', linewidth = 2)
plt.title('Elipse')
tiempoTranscurrido = time.time() - 0.5
print(f'Tiempo transcurrido en el bucle: {tiempoTranscurrido:.4f} s')
p = nAdentro/Nrandom
print(f'Probabilidad: {p:.4f}')
plt.show()

t0 = time.time()
X = np.random.rand(Nrandom)
Y = np.random.rand(Nrandom)
inside = ((X-0.5)**2)/(a**2) + ((Y-0.5)**2)/(b**2) < 1

plt.figure(2)
plt.scatter(X[inside], Y[inside], marker = '.', s = 0.5, color = 'blue', label = 'Adentro')
plt.scatter(X[~inside], Y[~inside], marker = '.', s = 0.5, color = 'red', label = 'Afuera')
plt.legend()


tiempoTranscurrido = time.time() - 0.5
print(f'Tiempo transcurrido en el bucle: {tiempoTranscurrido:.4f} s')
p = nAdentro/Nrandom
print(f'Probabilidad: {p:.4f}')
plt.show()