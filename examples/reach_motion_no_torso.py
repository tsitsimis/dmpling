import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from dmpling.dmp import DMP


# read data
data = np.loadtxt('../assets/Data_Sensor_1.dat', delimiter=' ', skiprows=5)

start = 4400
stop = 4800
step = 1
points = np.arange(start, stop, step)
position = data[points, 0:3]
n = position.shape[0]

# dmp
dt = 1e-2
T = n * dt
n_bfs = 1000
dmp_x = DMP(T, dt, n_bfs=n_bfs)
dmp_y = DMP(T, dt, n_bfs=n_bfs)
dmp_z = DMP(T, dt, n_bfs=n_bfs)

tau = 1.0
dmp_x.fit(position[:, 0], tau=tau)
dmp_y.fit(position[:, 1], tau=tau)
dmp_z.fit(position[:, 2], tau=tau)

goals = [position[-1, 0], position[-1, 1], position[-1, 2]]

pos_x = np.zeros(dmp_x.cs.N + 1)
pos_y = np.zeros(dmp_x.cs.N + 1)
pos_z = np.zeros(dmp_x.cs.N + 1)
pos_x[0], pos_y[0], pos_z[0] = position[0, 0], position[0, 1], position[0, 2]

k = 1.0
pos_x[1::] = dmp_x.run_sequence(k=k, tau=tau, goal=goals[0]-10)
pos_y[1::] = dmp_y.run_sequence(k=k, tau=tau, goal=goals[1]-15)
pos_z[1::] = dmp_z.run_sequence(k=k, tau=tau, goal=goals[2]+30)

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(position[:, 0], position[:, 1], position[:, 2], c='b')
ax.plot(pos_x, pos_y, pos_z, c='orange')
ax.scatter(position[0, 0], position[0, 1], position[0, 2], c='r', s=100)
ax.scatter(position[-1, 0], position[-1, 1], position[-1, 2], c='g', s=100)

ax.axis('equal')
plt.show()
