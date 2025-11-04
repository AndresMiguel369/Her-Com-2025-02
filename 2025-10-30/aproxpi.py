import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def estimarPi(N):
    dentro = 0
    for _ in range(N):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1: # criterio para definir el punto interno
            dentro += 1
    return 4 * dentro / N

# Parámetros
N = 1000
simulaciones = 5000

# Ejecutar simulaciones
estimaciones = [estimarPi(N) for _ in range(simulaciones)]

# Estadisticas
promedioPi = np.mean(estimaciones)
desviacionPi = np.std(estimaciones)

#Mostrar resultados

print(f"Estimación de pi: {promedioPi}")
print(f"Desviación estándar: {desviacionPi}")


# Estimación de pi
pi_estimado = estimarPi(N)

# Visualización

plt.figure(figsize=(10, 6))
sns.histplot(estimaciones, bins=50, kde=True, color='skyblue')
plt.axvline(promedioPi, color='red', linestyle='dashed', linewidth=0.8,
            label=f'Promedio: {promedioPi:.4f}')
plt.title(f'Distribución de estimaciones de pi (N={N}, simulaciones={simulaciones})')
plt.xlabel('Estimación de pi')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True)
plt.show()