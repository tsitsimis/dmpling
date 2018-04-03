import numpy as np
import c3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


# read data
reader = c3d.Reader(open('../assets/moc_s01_a06_r01.c3d', 'rb'))
data = reader.read_frames()
data = list(data)
n_frames = len(data)

# smooth data
data = [data[i][1][:, 0:3] for i in range(np.int(np.ceil(n_frames)))]
data = np.array(data)

data = savgol_filter(data, 401, 3, axis=0)
data = savgol_filter(data, 401, 3, axis=0)

# links
head = 0
back = np.arange(3, 7)
left_hand = np.arange(11, 19)
right_hand = [19, 20, 21, 22, 24]  # np.arange(19, 27)
left_leg = [27, 28, 30, 31, 32, 33, 34]
right_leg = [35, 37, 38, 39, 40, 41, 42]

# plot/animate
links = np.concatenate((np.array([0]), np.arange(3, 7), np.arange(11, 43)))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

points0 = data[0][:, 0:3]
for frame in np.arange(n_frames, step=50):
    ax.cla()
    points = data[frame][:, 0:3]

    ax.scatter(points[head, 0], points[head, 1], points[head, 2], c='orange', s=600)
    # ax.plot(points[back, 0], points[back, 1], points[back, 2], c='g', linewidth=10)
    ax.plot(points0[left_hand, 0], points0[left_hand, 1], points0[left_hand, 2], c='b', linewidth=10)
    ax.plot(points[right_hand, 0], points[right_hand, 1], points[right_hand, 2], c='b', linewidth=10)
    ax.plot(points0[left_leg, 0], points0[left_leg, 1], points0[left_leg, 2], c='y', linewidth=10)
    ax.plot(points0[right_leg, 0], points0[right_leg, 1], points0[right_leg, 2], c='m', linewidth=10)

    ax.axis('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_xlim(np.min(data[:, :, 0]), np.max(data[:, :, 0]))
    ax.set_ylim(np.min(data[:, :, 1]), np.max(data[:, :, 1]))
    ax.set_zlim(np.min(data[:, :, 2]), np.max(data[:, :, 2]))
    ax.grid(False)
    plt.draw()
    plt.pause(0.05)
