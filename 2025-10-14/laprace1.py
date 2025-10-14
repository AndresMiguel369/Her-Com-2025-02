import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0,1,101)
Y = np.linspace(0,1,101)

A,B = np.meshgrid(X,Y)
Psi = np.zeros(A.shape)

Psi[::,0] = 100
Psi[::,-1] = 80
Psi[-1,::] = 50
Psi[0,::] = 26
Error=[]

for ss in range(5000):
    Psi_new = np.copy(Psi)
    for i in range(1,len(X)-1):
        for j in range(1,len(Y)-1):
            Psi_new[i][j]=(Psi[i+1][j]+Psi[i][j+1]+Psi[i-1][j]+Psi[i][j-1])/4

    val = np.mean(abs(Psi_new-Psi).flatten())
    Error.append(val)
    if val<=1e-3:
        break
    Psi = np.copy(Psi_new)

plt.imshow(Psi)
plt.colorbar().set_label(label=r'$\Psi(x,y)$', size=20)
plt.xticks([],[])
plt.yticks([],[])
plt.xlabel('x', size=20)
plt.ylabel('y', size=20)
plt.show()