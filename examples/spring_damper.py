import numpy as np
import matplotlib.pyplot as plt


y0 = 1.3
g = 4
K = 150
D = 15
T = 2.0
dt = 1e-4

k = np.arange(0, T, dt)  # discrete time
N = k.shape[0]

y = y0
yd = 0
ydd = 0
y_traj = np.zeros(N) * y0
yd_traj = np.zeros(N)
ydd_traj = np.zeros(N)

for i in range(N):
    ydd = K * (g - y) - D * yd  # point attractor dynamics (PD controller)

    yd += ydd * dt
    y += yd * dt

    y_traj[i] = y
    yd_traj[i] = yd
    ydd_traj[i] = ydd

plt.plot(k, np.ones(N)*g, 'r--')
plt.plot(k, y_traj)
# plt.plot(k, yd_traj)
# plt.plot(k, ydd_traj)
plt.show()
