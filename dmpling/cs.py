import numpy as np


class CanonicalSystem:
    def __init__(self, a, T, dt):
        self.a = a
        self.T = T
        self.dt = dt

        self.time = np.arange(0, T, dt)
        self.N = self.time.shape[0]

        self.theta = None
        self.reset()

    def reset(self):
        self.theta = 1.0

    def step(self, tau=1.0):
        self.theta = self.theta - self.a * self.dt * self.theta / tau
        return self.theta

    def all_steps(self, tau=1.0):
        return np.array([self.step(tau) for _ in range(self.N)])

    # def step_(self):
    #     self.theta = np.exp(-self.a * self.dt) * self.theta
