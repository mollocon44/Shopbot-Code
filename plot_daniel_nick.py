''' This is cannibalizing Daniel's (and a little of Nick's) code to plot voxels. 
It definitely does a thing, and some of the voxels look fantastic, it just has a bug or two. '''

#The location of nodes within a cubic unit cell
#Units are relative to the voxel pitch
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import *

mat_matrix = np.ones((4,4,4))
vox_pitch = 1

uc_dims = [1.0,1.0,1.0]

node_locs = [[0.0,0.5,0.5],
             [0.5,0.0,0.5],  
             [0.5,0.5,0.0],
             [1.0,0.5,0.5],
             [0.5,1.0,0.5],
             [0.5,0.5,1.0]]

#References Node_locs, maps frame number to
#indices in node_locs corresponding to end-points
#The order of both the pairs and the IDs corresponds to 
#the Frame3dd convention of assigning endpoints
#see http://svn.code.sourceforge.net/p/frame3dd/code/trunk/doc/Frame3DD-manual.html
#Section 7.3

frame_locs = [[0,1],
              [0,2],
              [0,5],
              [0,4],
              [1,2],
              [1,5],
              [1,3],
              [2,4],
              [2,3],
              [5,3],
              [5,4],
              [4,3]]


def from_material():
    size_x = len(mat_matrix)
    size_y = len(mat_matrix[0])
    size_z = len(mat_matrix[0][0])
    node_frame_map = np.zeros((size_x,size_y,size_z,6))

    mat_dims = (np.array([size_x,size_y,size_z])-2)*uc_dims

    nodes = []
    frames = []
    cur_node_id = 0
    #Node Map Population
    #This builds the map of node IDs for each voxel.
    #The format is node_frame_map[x_coord_vox][y_coord_vox][z_coord_vox][id]
    #Since A voxel can share six nodes with its neighbors, sorting out which
    #voxel shares which nodes with which can be confusing
    #My approach right now is to assign IDs in a raster x>y>z, so there is
    #always a consistent notion of what nodes have been assigned, and which
    #are free.

    #ASIDE:
    #There are perhaps more efficient ways of distributing id's so that
    #the resulting stiffness matrix is as diagonal as possible 
    #That is, over all elements Ei with node ids ni1 and ni2, Sum(abs(ni2-ni1)) 
    #is minimized. 
    #For large numbers of nodes, this would be *extremely* useful.

    #To make ID assignment more compact, a 1-voxel border of empty voxels
    #surrounds the material matrix. That way, we can treat edges, corners and
    #vacancies as the same problem, from a node-assignment perspective.
    for i in range(1,size_x-1):
        for j in range(1,size_y-1):
            for k in range(1,size_z-1):
                node_ids = [0]*6
                if(mat_matrix[i][j][k] == 1):
                    if(mat_matrix[i-1][j][k] == 0):
                        nodes.append([(i+node_locs[0][0]-1)*vox_pitch,
                                      (j+node_locs[0][1]-1)*vox_pitch, 
                                      (k+node_locs[0][2]-1)*vox_pitch])
                        node_ids[0] = cur_node_id
                        cur_node_id = cur_node_id+1
                    else:
                        node_ids[0] = node_frame_map[i-1][j][k][3]

                    if(mat_matrix[i][j-1][k] == 0):
                        nodes.append([(i+node_locs[1][0]-1)*vox_pitch,
                                      (j+node_locs[1][1]-1)*vox_pitch, 
                                      (k+node_locs[1][2]-1)*vox_pitch])
                        node_ids[1] = cur_node_id
                        cur_node_id = cur_node_id+1
                    else:
                        node_ids[1] = node_frame_map[i][j-1][k][4]

                    if(mat_matrix[i][j][k-1] == 0):
                        nodes.append([(i+node_locs[2][0]-1)*vox_pitch,
                                      (j+node_locs[2][1]-1)*vox_pitch, 
                                      (k+node_locs[2][2]-1)*vox_pitch])
                        node_ids[2] = cur_node_id
                        cur_node_id = cur_node_id+1
                    else:
                        node_ids[2] = node_frame_map[i][j][k-1][5]

                    for q in range(3,6):
                        nodes.append([(i+node_locs[q][0]-1)*vox_pitch,
                                      (j+node_locs[q][1]-1)*vox_pitch, 
                                      (k+node_locs[q][2]-1)*vox_pitch])
                        node_ids[q] = cur_node_id
                        cur_node_id = cur_node_id+1
                    
                    node_frame_map[i][j][k][0:6] = node_ids

                    ### Frame Population
                    #Once The node IDs for a voxel have been found, we populate
                    #A list with the frame elements that compose the octahedron
                    #contained within a voxel
                    for q in range(0,12):
                        frames.append([node_ids[frame_locs[q][0]],
                                       node_ids[frame_locs[q][1]]])
                    #Constraints are added based on simple requirements right now
                    #The bottom-most nodes are constrained to neither translate nor
                    #rotate
    return nodes,frames

nodes,frames = from_material()




def plotLattice(nodes,frames):
    # Function to plot the intial lattice configuration
    # and the final version of the lattice configuration
    #
    # Input:    nodes - Initial node location
    #           frames - node frames
    #           res_displace - displacement of nodes
    #           scale - scaling parameter
    
    #intialize arrays
    xs = []
    ys = []
    zs = []
    

    
    #create plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('equal')
    frame_coords = []

    #poplate x, y, and z start and displacement arrays
    for i,node in enumerate(nodes):
	xs.append(node[0])
	ys.append(node[1])
	zs.append(node[2])


    # Add frame
    for i,frame in enumerate(frames):
	nid1 = int(frame[0])
	nid2 = int(frame[1])
	start = [xs[nid1],ys[nid1],zs[nid1]]
	end   = [xs[nid2],ys[nid2],zs[nid2]]
	
	ax.plot([start[0],end[0]],[start[1],end[1]],[start[2],end[2]],color='r', alpha=0.1)


    #plot
    ax.scatter(xs,ys,zs, color='r',alpha=0.1)

    plt.show()


plotLattice(nodes,frames)
