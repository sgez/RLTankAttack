'''
python 2.7 win32
'''
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def xyzfromarray(arr,y):
    how = len(arr) #y
    now = len(arr[0]) #x
    wlxs = list()
    wlys = list()
    wlzs = list()
    for i in range(0,how):
        for j in range (0,now):
            
            if arr[i][j]==True:
                wlzs.append(j)
                wlxs.append(i)
                wlys.append(y)
    return wlxs, wlys, wlzs

wl = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
    ], dtype=bool)


how = len(wl) #y
now = len(wl[0]) #x

ba = np.array([np.invert(wl), np.invert(wl)], dtype=bool)
ba[0][0][0] = 1 #position boat_0 to the left
ba[1][0][now - 1] = 1 #position boat_1 to the right

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

wlxs = list()
wlys = list()
wlzs = list()

wlxs,wlys,wlzs = xyzfromarray(ba[0],0)               
ax.scatter(wlxs, wlys, wlzs, s=100, c='r', marker='^')

wlxs,wlys,wlzs = xyzfromarray(ba[1],1)               
ax.scatter(wlxs, wlys, wlzs, s=100, c='g', marker='v')

wlxs,wlys,wlzs = xyzfromarray(wl,2)               
ax.scatter(wlxs, wlys, wlzs, s=100,c='b', marker='s')
'''
xs = [1,2,2,2,3,4,5,6,7,8,9,10]
ys = [1,1,1,1,1,1,1,1,1,1,1,1]
zs = zs[::-1]
ax.scatter(xs, ys, zs, c='g', marker='x')

xs = [1,2,3,4,5,6,7,8,9,10]
ys = [2,2,2,2,2,2,2,2,2,2]
zs = zs[::-1]
ax.scatter(xs, ys, zs, c='b', marker='x')
'''
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("Water Level(sqr) --- Boat 0(^) --- Boat 1(v)")
plt.show()
