import numpy as np
import matplotlib.pyplot as plt

delta_t = 0.001
t_max = 10
T = np.arange(0,t_max+delta_t,delta_t)

L = 1
V = 1

delta_x = V*delta_t

X=np.arange(0,L+delta_x,delta_x)

A,B = np.meshgrid(T,X)
Psi_sol = np.zeros(A.shape)
m = int((len(X)-1)/2)

Psi_sol[0,0] = 0
Psi_sol[0,0] = 0
Psi_sol[:m,0] = X[:m]
aux = np.ones(m)
aux = X[m]*aux*2
Psi_sol[m:-1,0] = aux-X[m:-1]

for i in range(1,len(X)-1):
    Psi_sol[i,1] = (Psi_sol[i+1,0]+Psi_sol[i-1,0])/2

for ii in range(2,len(T)):
    for jj in range(1,len(X)-1):
        Psi_sol[jj,ii] = Psi_sol[jj+1,ii-1] + Psi_sol[jj-1,ii-1] - Psi_sol[jj,ii-2]

plt.figure(figsize=(6, 2.5))
plt.imshow(Psi_sol, extent=(min(T),max(T),min(X),max(X)), aspect=5)
plt.ylabel(r'$x$', size=20)
plt.xlabel(r'$t$', size=20)
plt.colorbar().set_label(label=r'$\Psi(x,t)$', size=20)
plt.show()

plt.plot(X,Psi_sol[:,0])
plt.ylabel(r'$\Psi(x,0)$', size=20)
plt.xlabel(r'$x$', size=20)
plt.show()
