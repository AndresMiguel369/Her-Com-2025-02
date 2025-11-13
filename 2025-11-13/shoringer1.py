import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import time

N = 1000; w = 0.2; L = 50; h = L/(N-1); x = h*np.arange(N) - L/2
#print(x)

hbar = 1; mas = 1; tau = 0.5

ham = np.zeros((N,N), dtype = complex)
#print(ham.shape)

coef = (-hbar**2)/(2*mas*h**2)
for i in range(1, N-1):
    ham[i, i-1:i+2] = [coef, -2*coef, coef]
#print(ham)

ham[0, [-1, 0, 1]] = [coef, -2*coef, coef]
ham[-1, [-2, -1, 0]] = [coef, -2*coef, coef]
#print(ham)

dOscillator = np.diag(0.5*mas*(w**2)*(x**2))

I = np.eye(N)


A = I + 0.5j*(tau/hbar)*(ham + dOscillator)
B = I - 0.5j*(tau/hbar)*(ham + dOscillator)

dCN = np.linalg.inv(A)@ B

x0 = 0; vel = 0.01; k0 = mas*vel/hbar; sigma0 = L/10

NormPsi = 1/np.sqrt(sigma0*np.sqrt(np.pi))
psi = NormPsi*np.exp(1j*k0*x)*np.exp((-(x - x0)**2)/(2*sigma0**2))

maxIter = int(L/(vel*tau))
#print(maxIter)

n_time_steps = maxIter//10

probabilidad = np.zeros((N, n_time_steps))

t_values = np.zeros(n_time_steps)

start_time = time.time()
for i in range(n_time_steps):
    for _ in range(10):
        psi = dCN@psi
    
    psi = dCN@psi
    probabilidad[:, i] = np.abs(psi)**2
    t_values[i] = i*10*tau

elapse_time = time.time() - start_time
print(f'Tiempo de ejcucion: {elapse_time} segundos')

fig = plt.figure(figsize = (7, 5))
ax = fig.add_subplot(111, projection = '3d')

X,T = np.meshgrid(x, t_values)

surf = ax.plot_surface(X, T, probabilidad.T, cmap = 'viridis')
ax.view_init(elev = 30, azim = 50) #prespectiva

plt.show()