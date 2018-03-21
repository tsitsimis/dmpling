import numpy as np
from scipy import interpolate


def interpolate_path(dmp, path):
    time = np.linspace(0, dmp.cs.T, path.shape[0])
    inter = interpolate.interp1d(time, path)
    y = np.array([inter(i * dmp.dt) for i in range(dmp.cs.N)])
    return y


def calc_derivatives(y, dt):
    # velocity
    yd = np.diff(y) / dt
    yd = np.concatenate(([0], yd))

    # acceleration
    ydd = np.diff(yd) / dt
    ydd = np.concatenate(([0], ydd))

    return yd, ydd
