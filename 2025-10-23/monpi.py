import numpy as np

def random():
    x = np.random.rand()
    y = np.random.rand()
    return x,y

N = int(10000)
N_d = int(0)

for i in range(N):
    x,y = random()
    r = (x**2 + y**2)
    if (r <= 1):
        N_d = N_d + 1

result = 4*N_d/N

print(result)