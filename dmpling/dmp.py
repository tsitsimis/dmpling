"""
The code is based on the paper:

Pastor, P., Hoffmann, H., Asfour, T., & Schaal, S. (2009).
Learning and generalization of motor skills by learning from demonstration.
In 2009 IEEE International Conference on Robotics and Automation. IEEE.
https://doi.org/10.1109/robot.2009.5152385
"""

import numpy as np
from dmpling.cs import CanonicalSystem

from dmpling import utils


class DMP:
    def __init__(self, T, dt, a=150, b=25, n_bfs=10):
        self.T = T
        self.dt = dt
        self.y0 = 0.0
        self.g = 1.0
        self.a = a
        self.b = b
        self.n_bfs = n_bfs

        # canonical system
        a = 1.0
        self.cs = CanonicalSystem(a, T, dt)

        # initialize basis functions for LWR
        self.w = np.zeros(n_bfs)
        self.centers = None
        self.widths = None
        self.set_basis_functions()

        # executed trajectory
        self.y = None
        self.yd = None
        self.z = None
        self.zd = None

        # desired path
        self.path = None

        self.reset()

    def reset(self):
        if self.y0 is not None:
            self.y = self.y0  # .copy()
        else:
            self.y0 = 0.0
            self.y = 0.0
        self.yd = 0.0
        self.z = 0.0
        self.zd = 0.0
        self.cs.reset()

    def set_basis_functions(self):
        time = np.linspace(0, self.T, self.n_bfs)
        self.centers = np.zeros(self.n_bfs)
        self.centers = np.exp(-self.cs.a * time)
        self.widths = np.ones(self.n_bfs) * self.n_bfs ** 1.5 / self.centers / self.cs.a

    def psi(self, theta):
        if isinstance(theta, np.ndarray):
            theta = theta[:, None]
        return np.exp(-self.widths * (theta - self.centers) ** 2)

    def step(self, tau=1.0, k=1.0, start=None, goal=None):
        """
        executes one step of the DMP.
        :param start: start of movement
        :param goal: goal of executed trajectory
        :param tau: temporal scaling
        :param k: spatial scaling
        :return: position, velocity, acceleration of movement
        """
        if goal is None:
            g = self.g
        else:
            g = goal

        if start is None:
            y0 = self.y0
        else:
            y0 = start

        theta = self.cs.step(tau)
        psi = self.psi(theta)

        f = np.dot(self.w, psi) * theta * k * (g - y0) / np.sum(psi)

        self.zd = self.a * (self.b * (g - self.y) - self.z) + f  # transformation system
        self.zd /= tau

        self.z += self.zd * self.dt

        self.yd = self.z / tau
        self.y += self.yd * self.dt

        return self.y, self.yd, self.z, self.zd

    def fit(self, y_demo, tau=1.0):
        self.path = y_demo
        self.y0 = y_demo[0].copy()
        self.g = y_demo[-1].copy()

        y_demo = utils.interpolate_path(self, y_demo)
        yd_demo, ydd_demo = utils.calc_derivatives(y_demo, self.dt)

        f_target = tau**2 * ydd_demo - self.a * (self.b * (self.g - y_demo) - tau * yd_demo)
        f_target /= (self.g - self.y0)

        theta_seq = self.cs.all_steps()
        psi_funs = self.psi(theta_seq)

        # Locally Weighted Regression
        aa = np.multiply(theta_seq.reshape((1, theta_seq.shape[0])), psi_funs.T)
        aa = np.multiply(aa, f_target.reshape((1, theta_seq.shape[0])))
        aa = np.sum(aa, axis=1)

        bb = np.multiply(theta_seq.reshape((1, theta_seq.shape[0])) ** 2, psi_funs.T)
        bb = np.sum(bb, axis=1)
        self.w = aa / bb

        self.reset()
