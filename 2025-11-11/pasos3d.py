import numpy as np
import matplotlib.pyplot as plt

#Pasos en 3 dimensiones
pasos = np.random.choice([-1,1], size = (3,5000))
print(pasos.shape)
print(f"Dimensiones del arreglo : {pasos.shape}")

posicion = np.cumsum(pasos, axis = 1)

fig = plt.figure(figsize = (10,8))

ax = fig.add_subplot(111, projection = '3d')
ax.plot(posicion[0], posicion[1], posicion[2], color = 'blue', linewidth = 0.5)
ax.scatter(posicion[0, 0], posicion[1, 0], posicion[2, 0], color = 'green', s = 100, label = 'Inicio')
ax.scatter(posicion[0, -1], posicion[1, -1], posicion[2, -1], color = 'red', s = 100, label = 'Final')

ax.set_title('Caminata Aleatoria 3D', color = 'red', fontsize = 14, pad = 20)
ax.set_xlabel("Eje x")
ax.set_ylabel("Eje y")
ax.set_zlabel("Eje z")
ax.legend()
ax.grid(True)
plt.show()