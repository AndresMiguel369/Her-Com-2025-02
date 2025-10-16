import matplotlib.pyplot as plt
import numpy as np

delta_x=0.01
X=np.arange(-1,1+delta_x,delta_x)
len_x=len(X)

delta_t=delta_x**2
T=np.arange(0,0.1+delta_t,delta_t)
len_t=len(T)

Psi_sol=np.zeros([len_x,len_t])

m=int((len_x-1)/2)
Psi_sol[m][0] = 1/(2*delta_x)
Psi_sol[m-1][0] = 1/(4*delta_x)
Psi_sol[m+1][0] = 1/(4*delta_x)

for i in range(1,len_t):
    for j in range(1,len_x-1):
        Psi_sol[j][i]=(Psi_sol[j-1][i-1]+Psi_sol[j+1][i-1])/2

plt.imshow(Psi_sol,extent=(min(T), max(T), min(X), max(X)), aspect=0.04, vmin=0, vmax=3)
plt.xlabel(r'$t$', size=20)
plt.ylabel(r'$x$', size=20)
plt.colorbar()
plt.show()