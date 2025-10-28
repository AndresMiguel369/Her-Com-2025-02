import numpy as np
import matplotlib.pyplot as plt
"""a = np.arange(0,10)

b = (4 + 3*a)%5

print(b)"""

"""c = [x%12 for x in range(1,14)]

print(c)"""

"""semilla = 7182

def aleatorio(semilla):
  #global semilla
  s1 = str(semilla**2)
  while len(s1) != 8:
    s1 = "0" + s1
  semilla =  int(s1[2:6])
  return semilla

for i in range(9):
  semilla = aleatorio(semilla)
  #print(semilla)
"""  

def rng(m = 2**32, a = 123456789, c = 12345):
  rng.corriente=(a*rng.corriente + c)%m
  return rng.corriente/m

rng.corriente = 123456789

"""d = [rng() for i in range(10)]
print(d)"""

N = 50000
muestras = np.array([rng() for _ in range(N)])

plt.figure(figsize = (9,3))
plt.plot(muestras[:500], lw=0.8)
plt.title('Serie - Primeras 500 entradas generadas por rng')
plt.xlabel('t')
plt.ylabel('p(t)')
plt.tight_layout()
plt.show()

u = muestras[:-1]
v = muestras[1:]

plt.figure()
plt.scatter(u, v, s = 1, alpha = 0.5)
plt.title('2d pares consecutivos')
plt.xlabel('p(t)')
plt.ylabel('p(t+1)')
plt.axis('equal')
plt.show()

plt.figure(figsize = (5,3))
bins = 50
plt.hist(muestras, bins = bins, density = True, alpha = 0.7, label = 'empirico')
x = np.linspace(0,1,200)
plt.plot(x, np.ones_like(x), 'r', label = 'uniforme')
plt.title('Histograma (%d bins, %d muestras )'%(bins, N))
plt.xlabel('p(t)')
plt.ylabel('densidad')
plt.legend()
plt.tight_layout()
plt.show()