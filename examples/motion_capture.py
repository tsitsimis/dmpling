import numpy as np
import c3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


# read data
reader = c3d.Reader(open('../assets/moc_s01_a06_r01.c3d', 'rb'))
frames = reader.read_frames()
frames = list(frames)
n_frames = len(frames)

# read human's hand points
dof = 23
points = [frames[i][1][dof, 0:3] for i in range(np.int(np.ceil(n_frames/7)))]
points = np.array(points)

# smooth raw points
smoothed = savgol_filter(points, 401, 3, axis=0)
smoothed = savgol_filter(smoothed, 401, 3, axis=0)

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(smoothed[:, 0], smoothed[:, 1], smoothed[:, 2], s=1)
ax.scatter(smoothed[0, 0], smoothed[0, 1], smoothed[0, 2], c='r')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.axis('square')
plt.show()

exit()
# points = frames[1][1][:, 0:3]
# points = np.array(points)
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(points[:, 0], points[:, 1], points[:, 2])
# p = 23
# ax.scatter(points[p, 0], points[p, 1], points[p, 2], c='r', s=50)
# ax.axis('square')
# plt.show()
