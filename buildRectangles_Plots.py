''' Clumsy first attempt at integrating the cuboct plotting into the whole graph.

	Doesn't work. '''


## optimized for test9.sbp 8/30


import shopbot_base_programs as sbp
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib.path import Path
import random
import time




random.seed()

   #sample 3dplot code
''' threeDfig = plt.figure()
    ax = threeDfig.add_subplot(111, projection='3d')
    ax.plot(x,y,z) '''


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b)


vox_plot = plt.figure()   
ax = p3.Axes3D(vox_plot)	 
ax.set_xlim3d(0, 5)				
ax.set_ylim3d(0, 5)
ax.set_zlim3d(0, 5)
### formerly: ax = vox_plot.add_subplot(111, projection='3d')
xs,ys,zs = [],[],[]

plt.ion()

x_dim,y_dim,z_dim = 3,3,3
seed_crystal = 0
print sbp.header

print "\n\'\'rectangle size " +str((x_dim,y_dim,z_dim)) + '\n'

#############################################################
# correct number of steps to build a generic rectangular 	#
# prism. 													#
# it takes x_dim + y_dim - 1 diagonals to complete a layer, #
# and it takes z_dim - 1 steps before the last layer begins	#
#############################################################
steps = x_dim + y_dim + z_dim - 2    



######################################################################
######################################################################
## Our function buildDiagonal(step, layer) takes in a step number 	##   ## THIS IS WHAT SHOULD BE MODIFIED FOR RECTANGLES ##
## (step being defined as a single ordered pass through each layer)	##
## and a layer, and it outputs a list of the diagonal blocks to add	##
## to that layer during that step 									##
######################################################################
######################################################################
def buildDiagonal(step, layer): 
	diagonal_number = step - layer
	if diagonal_number < 0 : #dealing with layers when we don't want anything built
		return

	## the quantity offset determines how many rows need to be skipped in the x and y directions in each diagonal step. ##
	x_offset = diagonal_number - y_dim + 1
	y_offset = diagonal_number - x_dim + 1

	blocksToPlace = [] #initializes empty list to store coordinates of blocks for that step & layer
		
	## initial boundary conditions ##
	if x_offset < 0: 
		x_offset = 0  	
	if y_offset < 0:
		y_offset = 0

	x = x_offset 




	''' add each block to blocksToPlace, decreasing y by 1 and increasing x by 1 each time.

		build order is important.  '''

	for y in range(diagonal_number - x_offset, y_offset-1 , -1) :
		#print 'd = ' + str(diagonal_number) ###																						###
		blocksToPlace.append((x,y,layer))   ###  NOTE: if for some reason x were not a reliable indicator for where to stop building,  ###
										   ###		 y should stop at min(diagonal_number,y_dim-1)								 	  ###
		x += 1							  ###																						 ###


	if step >= seed_crystal:
		buildBlocks(blocksToPlace)
	return



sb_zero_offset = 1 # shopbot zeros to voxel 1,1,1 not 0,0,0
				   # we will subtract this later

## cuboct_verts based on Daniel Celluci's code pfea/src/cuboct.py
## would be more elegant as its own Class but I don't have that kind of time right now
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
				
def plot_cuboct(dx,dy,dz):
	ax = p3.Axes3D(vox_plot)

	global xs,ys,zs

	for (x,y,z) in cuboct_verts:
		xs.append(x+dx)
		ys.append(y+dy)
		zs.append(z+dz)

	ax.plot(xs, ys, zs, zdir='z', c='b')



##########################################################################
##########################################################################
## Eventually, buildBlocks(blocksToPlace) will take in a list of 		##
## blocksToPlace and output the shopbot code needed to place the blocks ##
## coordinates (x,y,z) in the correct order. It doesn't do this yet,	##
## however, as the shopbot code has not been finalized. 				##
##########################################################################
##########################################################################
def buildBlocks(blocksToPlace):  #for testing purposes, prints out a list of blocks to attach during each step (in order)
	
	for (x,y,z) in blocksToPlace:
		print "\'\' NEXT VOXEL = "+str((x,y,z))
		dx = -76.2*(x - sb_zero_offset) #76.2 is the conversion factor from 3in to mm
		dy = -76.2*(y - sb_zero_offset)
		dz = 76.2*(z - sb_zero_offset)
		'''  PLACEMENTS AND ATTACHMENTS 
		if z > 0 :
			print "\n\'\'\'\'\'Place and attach z\n"
			print sbp.position_attach_z(dx,dy,dz)
			if y > 0 :
				print "\n\'\'\'\'attach y"   ## y then x, directionality is important
				print sbp.attach_y(dx,dy,dz) 
			if x > 0: 
				print "\n\'\'\'\'attach x"
				print sbp.attach_x(dx,dy,dz)
		elif y > 0:
			print "\n\'\'\'\'Place and attach y\n"
			print sbp.position_attach_y(dx,dy,dz)
			if x > 0: 
				print "\n\'\'\'\'attach x"
				print sbp.attach_x(dx,dy,dz)
		elif x > 0: 
			print "\n\'\'\'\'\'Place and attach x\n"
			print sbp.position_attach_x(dx,dy,dz)'''
		
		#xs.append(x)
		#ys.append(y)
		#zs.append(z)
	
		plot_cuboct(x,y,z)

	plt.pause(0.6)
	

	#print '\n'
	return



for step in range(steps):
	for layer in range(z_dim) : # build bottom up, directionality important
		#print 'step = ' + str(step)
		#print 'layer = ' + str(layer)
		buildDiagonal(step, layer)
print "\nEND"
#print sbp.end_effector_programs
plt.ioff()
plt.show()





