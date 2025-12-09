import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
#from IPython.display import HTML
#from matplotlib import rc

#Constantes universales(unitarias)
hbar = 1
m = 1

#limites de la "caja", tiempo y numero de discretizacion
t_inicial = 0.0
t_final = 2.4
Nt = 240

x_min, x_max = -20.0, 20.0
y_min, y_max =  -20.0, 20.0
Nx = 401
Ny = 401

#discretizacion del espacio y el tiempo
dx = (x_max - x_min) / (Nx - 1)
dy = (y_max - y_min) / (Ny - 1)
dt = (t_final - t_inicial)/Nt

X = np.linspace(x_min, x_max, Nx)
Y = np.linspace(y_min, y_max, Ny)
T = np.arange(t_inicial, t_final, dt)

#psi como arreglo que tiene los valores de la funcion de onda en la posicion (x,y) en el tiempo

Psi = np.zeros((Nx, Ny, Nt), dtype = complex)

#discretizacion del espacio momento
k_x = 2 * np.pi * np.fft.fftfreq(Nx, dx)
k_y = 2 * np.pi * np.fft.fftfreq(Ny, dy)
Kx, Ky = np.meshgrid(k_x, k_y)

#condiciones iniciales
D, E = np.meshgrid(X, Y)
V = np.zeros(D.shape)

#Doble rendija
#x_R, tam_R = -0.25, 0.5
#y_h1, y_h2, tam_h = -0.2, 0.2, 0.3
#ix0, ix1 = int((x_R - x_min)/dx), int((x_R + tam_R - x_min)/dx)
#iyh10, iyh11 = int((y_h1 - tam_h - y_min)/dy), int((y_h1 - y_min)/dy)
#iyh20, iyh21 = int((y_h2 - y_min)/dy), int((y_h2 + tam_h - y_min)/dy)
#V[:iyh10, ix0:ix1+1] = 50.0
#V[iyh11+1:iyh20, ix0:ix1+1] = 50.0
#V[iyh21+1:, ix0:ix1+1] = 50.0

#dos placas como potencial (tambien puede para un cuadrado)
#bx0, bx1 = -3.0, 3.0
#by0, by1 = -3.0, 3.0
#ix0, ix1 = int((bx0 - x_min)/dx), int((bx1 - x_min)/dx)
#iy0, iy1 = int((by0 - y_min)/dy), int((by1 - y_min)/dy)
#V[iy0:iy1+1, ix0:ix0+11] = 10.0
#V[iy0:iy1+1, ix1:ix1+11] = 10.0

#solo una placa
#bx0, bx1 = -1.0, 1.0
#ix0, ix1 = int((bx0 - x_min)/dx), int((bx1 - x_min)/dx)
#V[:, ix0:ix1+1] = 5.0


# Condiciones iniciales(posicion y momento inicial de la particula) y creacion de la funcion de onda(Psi_0)
x0, y0 = -3.0, 0.0
estx, esty = 0.8, 0.8
px0, py0 = 10.0, 0.0

Psi_0 = np.exp(-((D-x0)**2/(2*estx))-((E-y0)**2/(2*esty))) * np.exp(1j*(px0*D + py0*E)/hbar)
aux = (dx**2)*(np.abs(Psi_0)**2)
Norma = np.sqrt(np.sum(aux))
Psi_0 = Psi_0/Norma
Psi[:, :, 0] = Psi_0

#operadores para hacer los pasos de tiempo
H_k = ((hbar**2)/(2*m))*(Kx**2 + Ky**2)
Uk_dt = np.exp((-1j*H_k*dt)/hbar)
H_r = V
Ur_dtmedios = np.exp((-1j*H_r*dt)/(2*hbar))

#Paso del tiempo
start = time.time()
for i in range(len(T)-1):

  Psi_new = Psi[:, :, i]
  Psi_new = Psi_new * Ur_dtmedios

  Psi_new2 = np.fft.fft2(Psi_new)
  Psi_new2 = Psi_new2 * Uk_dt

  Psi_new = np.fft.ifft2(Psi_new2)
  Psi_new = Psi_new * Ur_dtmedios

  Psi[:, :, i+1] = Psi_new

Prob = np.abs(Psi)**2

end = time.time()
print("Tiempo total del algoritmo:", end - start, "s")

#Comprobar la norma
def norm(psi):
    return np.sqrt(np.sum(np.abs(psi)**2) * dx * dy)

print("Norma inicial:", norm(Psi[:, :, 0]))
print("Norma final:", norm(Psi[:, :, -1]))
print("Densidad de probabilidad inicial:", (norm(Psi[:, :, 0])**2))
print("Densidad de probabilidad final:", (norm(Psi[:, :, -1])**2))

#animacion
#              limites de visualizacion
x_minvis, x_maxvis = -10.0, 10.0
y_minvis, y_maxvis = -10.0, 10.0
ix_minvis, ix_maxvis = int((x_minvis - x_min)/dx), int((x_maxvis - x_min)/dx)
iy_minvis, iy_maxvis = int((y_minvis - y_min)/dy), int((y_maxvis - y_min)/dy)

fig, ax = plt.subplots(figsize=(7,5))

#              Mostrar el primer frame
img = ax.imshow(Prob[ix_minvis:ix_maxvis+1, iy_minvis:iy_maxvis+1, 0], cmap='viridis', origin='lower', extent=[x_minvis, x_maxvis, y_minvis, y_maxvis])

#              Mostrar el potencial
V_graficar = V[ix_minvis:ix_maxvis+1, iy_minvis:iy_maxvis+1]
V_graficar[V_graficar == 0] = np.nan
def init():
  imgV = ax.imshow(V_graficar, cmap="inferno", origin="lower", extent=[x_minvis, x_maxvis, y_minvis, y_maxvis], alpha = 0.35)
  return [imgV]

ax.set_title("Probabilidad |psi|^2 en el tiempo")
ax.set_xlabel("x")
ax.set_ylabel("y")

#               Barra de colores
cbar = fig.colorbar(img, ax = ax, location = 'right')
cbar.set_label("Probabilidad")

#               Función de actualización
def update(frame):
    #print("frame pedido:", frame)
    img.set_data(Prob[ix_minvis:ix_maxvis+1, iy_minvis:iy_maxvis+1, frame])
    ax.set_title(f"Tiempo t = {T[frame]:.3f}")
    return [img]

#               Construcción de la animación
#from matplotlib import rc
#rc('animation', html='jshtml')

anim = FuncAnimation(
    fig,
    update,
    init_func = init,
    frames=range(0, len(T), 5),
    interval = 70,   # velocidad (ms)
    blit=False
)
#plt.close(fig)

"""from matplotlib.animation import FuncAnimation, FFMpegWriter

writer = FFMpegWriter(fps=18, bitrate=1800)
anim.save("onda_2d.mp4", writer=writer)

HTML(anim.to_jshtml())"""

plt.show()