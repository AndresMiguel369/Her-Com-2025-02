import numpy as np
import matplotlib.pyplot as plt

N = 100000
inside = 0
aproximacion = np.empty(N)
for i in range(N):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    if np.sqrt(x**2 + y**2) <= 1:
        inside = inside + 1
    aproximacion[i] = 4 * inside / (i+1)

plt.figure(figsize=(10,4))
plt.semilogx(aproximacion)
plt.axhline(np.pi,color='red',linestyle='--')
plt.xlabel('Número de Iteraciones')
plt.ylabel('Aproximación de pi')
plt.title('Aproximación de pi a través de iteraciones')
plt.show()