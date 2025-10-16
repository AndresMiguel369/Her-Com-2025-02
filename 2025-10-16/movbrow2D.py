import numpy as np
import matplotlib.pyplot as plt

def Coin():
    s = np.random.rand()
    h = s*2*np.pi

    return h

delta_r = 0.01

for i in range(1000):
    posx = 0
    posy = 0
    X = [posx]
    Y = [posy]
    for j in range(1000):
        posx = posx + np.sin(Coin())*delta_r
        posy = posy + np.cos(Coin())*delta_r
        X.append(posx)
        Y.append(posy)
    plt.plot(X,Y, linewidth=0.1, alpha=0.5)

plt.axis('off')
plt.show()