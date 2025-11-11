import numpy as np
import matplotlib.pyplot as plt

num_caminantes = 1000
num_pasos = 5000
dimension = 2

pasos = np.random.choice([-1, 1], size = (num_caminantes, dimension, num_pasos))
posiciones = np.cumsum(pasos, axis = 2)

distancias_cuadradas = posiciones[:, 0, :]**2 + posiciones[:, 1, :]**2
rms = (np.mean(distancias_cuadradas, axis = 0))

plt.figure(figsize = (10,6))
pasos_range = np.arange(1, num_pasos + 1)
plt.plot(pasos_range, rms, color = 'blue', linewidth = 2, label = 'RMS simulado')

plt.ylabel(r'Raiz media cuadratica $\langle(x² + y²)\rangle$', fontsize = 12)
plt.xlabel('Numero de pasos', fontsize = 12)
plt.grid(True, alpha = 0.3)
plt.legend(fontsize = 12)
plt.tight_layout()
plt.show()