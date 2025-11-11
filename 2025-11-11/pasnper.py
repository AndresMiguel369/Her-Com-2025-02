import numpy as np
import matplotlib.pyplot as plt

num_caminantes = 1000
num_pasos = 5000
dimension = 2

pasos = np.random.choice([-1, 1], size = (num_caminantes, dimension, num_pasos))

posiciones = np.cumsum(pasos, axis = 2)
posiciones_finales = posiciones[:,:,-1]

x_final = posiciones_finales[:,0]
y_final = posiciones_finales[:,1]
#z_final = posiciones_finales[2]

distancia = np.sqrt(x_final**2 + y_final**2) 

fig, axes = plt.subplots(1, 3, figsize = (18,5))

axes[0].hist(x_final, bins = 50, color = 'blue', alpha = 0.7, edgecolor = 'black')
axes[0].set_title('Distribucion de posicion en x', fontsize = 12)
axes[0].grid(True, alpha= 0.3)

axes[1].hist(y_final, bins = 50, color = 'red', alpha = 0.7, edgecolor = 'black')
axes[1].set_title('Distribucion de posicion en y', fontsize = 12)
axes[1].grid(True, alpha= 0.3)

axes[2].hist(distancia, bins = 50, color = 'green', alpha = 0.7, edgecolor = 'black')
axes[2].set_title('Distribucion de posicion en distancias', fontsize = 12)
axes[2].grid(True, alpha= 0.3)

plt.show()
