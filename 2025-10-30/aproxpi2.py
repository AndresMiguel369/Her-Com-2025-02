import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

N = 2000
inside = []
for i in range(N):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    if np.sqrt(x**2 + y**2) <= 1:
        inside.append((x,y))
plt.figure(figsize=(4,4))
plt.scatter([x[0] for x in inside],[x[1] for x in inside],
            color = 'blue',marker='.',alpha=0.5)
plt.show()