import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('characters_moby.txt', dtype = str)

C_list, Freq = np.unique(data,return_counts=True)

V = ['a','e','i','o','u']

States = []

for x in data:
    if x in V:
        s = 0
    else:
        s = 1
    
    States.append(s)

Transition = np.zeros([2,2])

for i in range (len(States)-1):
    val1 = States[i]
    val2 = States[i+1]
    Transition[val1][val2] += 1

matW = np.zeros([2,2])

for i in range(2):
    matW[i] = Transition[i]/sum(Transition[i])

plt.imshow(matW)
plt.xticks([0,1],['V','C'])
plt.yticks([0,1],['V','C'])
plt.colorbar()
plt.show()

States_V = []

for x in data:
    if x in V:
        States_V.append(V.index(x))

Transition2 = np.zeros([5,5])

for i in range(len(States_V)-1):
    val1 = States_V[i]
    val2 = States_V[i+1]
    Transition2[val1][val2] += 1

matW2 = np.zeros([5,5])

for i in range(5):
    matW2[i] = Transition2[i]/sum(Transition2[i])

plt.imshow(matW2)
plt.xticks(list(range(5)),V)
plt.yticks(list(range(5)),V)
plt.colorbar()
plt.show()  


