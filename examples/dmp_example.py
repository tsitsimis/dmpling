import matplotlib.pyplot as plt
import numpy as np

from dmpling.dmp import DMP

y0 = 1.3
g = 4
K = 100
D = 20
T = 2.0
dt = 1e-4
n_bfs = 10

dmp = DMP(T, dt, n_bfs=n_bfs)

N = dmp.cs.N
y = np.zeros(N)
for i in range(N):
    y[i], _, _, _ = dmp.step()

plt.plot(dmp.cs.time, y)
plt.show()
