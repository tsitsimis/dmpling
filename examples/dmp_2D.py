import matplotlib.pyplot as plt
import numpy as np

from dmpling.dmp import DMP

T = 2.0
dt = 1e-2
a = 10
b = a / 4
n_bfs = 100

t = np.arange(0, T, dt)
f = 1 / T
path2 = np.sin(2*np.pi*f*t)
path1 = np.cos(2*np.pi*f*t)

# define dmps
dmp1 = DMP(T, dt, n_bfs=n_bfs, a=a, b=b)
dmp1.fit(path1)

dmp2 = DMP(T, dt, n_bfs=n_bfs, a=a, b=b)
dmp2.fit(path2)

# run
y1 = np.zeros(dmp1.cs.N)
y2 = np.zeros(dmp1.cs.N)

for i in range(dmp1.cs.N):
    y1[i], _, _, _ = dmp1.step(k=1.5)
    y2[i], _, _, _ = dmp2.step(k=1.5)

plt.plot(path1, path2)
plt.plot(y1, y2)

plt.axis('equal')
plt.xlim([path1.min()*2, path1.max()*2])
plt.ylim([path2.min()*2, path2.max()*2])
plt.show()

exit()
for i in range(dmp1.cs.N):
    y1[i], _, _, _ = dmp1.step()
    y2[i], _, _, _ = dmp2.step()
    plt.scatter(y1[i], y2[i], c='orange')
    plt.pause(0.02)
