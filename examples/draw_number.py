import matplotlib.pyplot as plt
import numpy as np

from dmpling.dmp import DMP

data = np.load('../assets/number2.npy')

path1 = data[:, 0]
path2 = data[:, 1]
n = path1.shape[0]

# define dmps
dt = 1e-2
T = n * dt
a = 10
b = a / 4
n_bfs = 100

dmp1 = DMP(T, dt, n_bfs=n_bfs, a=a, b=b)
dmp1.fit(path1)

dmp2 = DMP(T, dt, n_bfs=n_bfs, a=a, b=b)
dmp2.fit(path2)

# run
y1 = np.zeros(dmp1.cs.N)
y2 = np.zeros(dmp1.cs.N)

# s1 = path1[0] + 0.7
# s2 = path2[0] - 0.8
# dmp1.y = s1
# dmp2.y = s2
#
# g1 = path1[-1] + 0.7
# g2 = path2[-1] - 0.8

k = 1.3
for i in range(dmp1.cs.N):
    y1[i], _, _, _ = dmp1.step(k=k)
    y2[i], _, _, _ = dmp2.step(k=k)

# plot
plt.plot(path1, path2)
plt.plot(y1, y2)

plt.axis('equal')
plt.xlim([path1.min()*2, path1.max()*2])
plt.ylim([path2.min()*2, path2.max()*2])
plt.show()
