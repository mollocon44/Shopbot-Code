''' Takes in dimensions of a rectangular prism (x_dim,y_dim,z_dim)
and prints out the shopbot code to build it (minus seed crystal)
'''

''' Sorry it's the messy one, I'm taking my time to do the pretty version properly.'''
''' If you need me, my email is oconnormollyc@gmail.com '''

''' IMPLEMENTATION: python bruteRectangleSBP.py > filename.sbp '''

## optimized for test9.sbp 8/30


import shopbot_base_programs as sbp

x_dim,y_dim,z_dim = 3,3,3
seed_crystal = 2
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
## Our function buildDiagonal(step, layer) takes in a step number 	##   
## (step being defined as a single ordered pass through each layer)	##
## and a layer, and it outputs a list of the diagonal blocks to add	##
## to that layer during that step 									##
######################################################################
######################################################################
def buildDiagonal(step, layer): 
	diagonal_number = step - layer
	if diagonal_number < 0 : #dealing with layers when we don't want anything built
		return

	## the quantity i_offset determines how many rows need to be skipped in the x and y directions in each diagonal step. ##
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

		build order is important (at least while the servo is in the way. Is build order still important 
		for gripper 2.0?  '''

	for y in range(diagonal_number - x_offset, y_offset-1 , -1) :
											 ###																						###
		blocksToPlace.append((x,y,layer))   ###  NOTE: if for some reason x were not a reliable indicator for where to stop building,  ###
										   ###		 y should stop at min(diagonal_number,y_dim-1)								 	  ###
		x += 1							  ###																						 ###


	if step >= seed_crystal:
		buildBlocks(blocksToPlace)
	return



sb_zero_offset = 1 # shopbot zeros to voxel 1,1,1 not 0,0,0
				   # we will subtract this later



##########################################################################
##########################################################################
## buildBlocks(blocksToPlace) will takes in a list blocksToPlace in the ##
## current diagonal and outputs the shopbot code (with appropriate 		##
## comments) needed to place the blocks, coordinates (x,y,z), in the 	##
## correct order. It is called by buildDiagonal							##
##########################################################################
##########################################################################
def buildBlocks(blocksToPlace):  #for testing purposes, prints out a list of blocks to attach during each step (in order)
	for (x,y,z) in blocksToPlace:
		print "\'\' NEXT VOXEL = "+str((x,y,z))
		dx = -76.2*(x - sb_zero_offset) #76.2 is the conversion factor from 3in to mm
		dy = -76.2*(y - sb_zero_offset)
		dz = 76.2*(z - sb_zero_offset)
		'''  PLACEMENTS AND ATTACHMENTS '''
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
			print sbp.position_attach_x(dx,dy,dz)
		
		

	print '\n'
	return




for step in range(steps):
	for layer in range(z_dim) : # build bottom up, directionality important
		buildDiagonal(step, layer)
print "\nEND"
print sbp.end_effector_programs

