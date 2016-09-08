
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3




## node_locs is taken from Daniel Celluci's code pfea/src/cuboct.py

#Geometric Properties

#The location of nodes within a cubic unit cell
#Units are relative to the voxel pitch

'''node_locs = [[0.0,0.5,0.5],
			 [0.5,0.0,0.5],  
			 [0.5,0.5,0.0],
			 [1.0,0.5,0.5],
			 [0.5,1.0,0.5],
			 [0.5,0.5,1.0]]'''




cuboct_verts = [(0.5,0.5,0.0),
				(0.5,0.0,0.5),
				(0.5,0.5,1.0),
				(0.5,1.0,0.5),
				(0.5,0.5,0.0),
				(1.0,0.5,0.5),
				(0.5,0.5,1.0),
				(0.0,0.5,0.5),
				(0.5,1.0,0.5),
				(1.0,0.5,0.5),
				(0.5,0.0,0.5),
				(0.0,0.5,0.5),
				(0.5,0.5,0.0)]

fig = plt.figure()
ax = p3.Axes3D(fig)

xs,ys,zs=[],[],[]

for (x,y,z) in cuboct_verts:
	xs.append(x)
	ys.append(y)
	zs.append(z)

ax.plot(xs, ys, zs, zdir='z', c='b')


plt.show()
