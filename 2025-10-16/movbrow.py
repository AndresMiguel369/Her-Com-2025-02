import numpy as np
import matplotlib.pyplot as plt

def Coin():
    z = np.random.rand()
    if z <= 0.5:
        out = -1
    else:
        out = +1

    return out

delta_x = 0.01

delta_t=delta_x**2
T=np.arange(0,0.1+delta_t,delta_t)
len_t=len(T)

for i in range(10000):
    pos = 0
    X = [pos]
    for j in range(1000):
        pos = pos + Coin()*delta_x
        X.append(pos)
    plt.plot(T,X, linewidth=0.1, alpha=0.5)

plt.show()