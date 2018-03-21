import matplotlib.pyplot as plt
import numpy as np

from dmpling import cs as CanSys

tau = 1.0
a = 10.0
T = 1.0
dt = 1e-2
cs = CanSys.CanonicalSystem(a, T, dt)

n = cs.N

vals = np.zeros(n)
for i in range(n):
    vals[i] = cs.step(tau)

plt.plot(vals)
plt.show()
