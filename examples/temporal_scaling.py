import matplotlib.pyplot as plt
import numpy as np

from dmpling.dmp import DMP

T = 6.0
dt = 1e-2
a = 10
b = a / 4
n_bfs = 1000

t = np.arange(0, T, dt)
path1 = np.sin(2 * t)
path2 = np.zeros(path1.shape)
path2[int(len(path2)/2.):] = 0.5
path3 = 1 / (1 + np.exp(-10*t))
path4 = 1 - (-0.9*t**3 + 3*t**2 - 2) / (1 + np.exp(10*(t-2)))
path = path4

tau = 0.8
k = 1.0
dmp = DMP(T, dt, n_bfs=n_bfs, a=a, b=b)
dmp.fit(path, tau=1.0)

y = np.zeros(dmp.cs.N)
yd = np.zeros(dmp.cs.N)
z = np.zeros(dmp.cs.N)
zd = np.zeros(dmp.cs.N)

for i in range(dmp.cs.N):
    y[i], yd[i], z[i], zd[i] = dmp.step(tau=tau, k=k)

# plot
plt.plot(path)
plt.plot(y)
plt.show()
