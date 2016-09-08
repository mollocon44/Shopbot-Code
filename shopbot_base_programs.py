## updated for test9.sbp

### This is the message box version. It has pop-up windows for reloading, rather than our usual death-defying pausing method
### It's entirely possible that the line after the message box wants to deal with the answer to the message box.
### If that's the case, it should need to be:
### 	IF &msganswer = "OK" THEN ...[Whatever you were going to have it do next anyway]
### but I think it should be okay as is...   godspeed.

##################################################################
## This is the OpenSBP used for controlling the end effector,   ##
## written by Grace and Greenfield, with some tweaking by all 3 ##
## of us. It's called by buildRectangles.py                     ##
##      DO NOT EDIT THIS WITHOUT GREENFIELD'S PERMISSION.       ##
##################################################################

off_camera = 300 #coordinate used to send end effector off camera for voxel and bolt reloading
header = "\nSA \'\'\'\'sets absolute coordinates\n"

end_effector_programs = """
OpenJaws:
	SO, 6, 1
	SO, 2, 1
	SO, 3, 0
	SO, 5, 0
	SO, 7, 0
	PAUSE 1
	SO, 6, 0
	PAUSE 1
	RETURN

CloseJaws:
	SO, 6, 1
	SO, 2, 0
	SO, 3, 1
	SO, 5, 0
	SO, 7, 0
	PAUSE 1
	SO, 6, 0
	PAUSE 1
	RETURN

Bolt:

	SO, 6, 1
	SO, 2, 1
	SO, 3, 1
	SO, 5, 0
	SO, 7, 0
	PAUSE 1
	SO, 6, 0
	PAUSE 8
	RETURN

EngageGripper:
	SO, 6, 1
	SO, 2, 0
	SO, 3, 0
	SO, 5, 1
	SO, 7, 0
	PAUSE 1
	SO, 6, 0
	PAUSE 3
	RETURN

DisengageGripper:
	SO, 6, 1
	SO, 2, 1
	SO, 3, 0
	SO, 5, 1
	SO, 7, 0
	PAUSE 1
	SO, 6, 0
	PAUSE 1.5
	RETURN

OpenJawsHalf:
	SO, 6, 1
	SO, 2, 0
	SO, 3, 1
	SO, 5, 1
	SO, 7, 0
	PAUSE 1
	SO, 6, 0
	PAUSE 1
	RETURN

CloseJawsHalf:
	SO, 6, 1
	SO, 2, 1
	SO, 3, 1
	SO, 5, 1
	SO, 7, 0
	PAUSE 1
	SO, 6, 0
	PAUSE 1
	RETURN

Unbolt:
	SO, 6, 1
	SO, 2, 0
	SO, 3, 0
	SO, 5, 0
	SO, 7, 1
	PAUSE 1
	SO, 6, 0
	PAUSE 6
	RETURN


"""




def position_attach_z(dx,dy,dz):
	return """
M5 """ + str(-75) + """, """ + str(-off_camera) + """, """ + str(75) + """, 0, 0
\'\'Reload bolt and voxel
MSGBOX( Click OK to continue,64,Reload bolt and voxel!)
GOSUB EngageGripper 

M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75+dz) + """, 0, 0
M5 """ + str(-30+dx) + """, """ + str(-30+dy) + """, """ + str(24+dz) + """, 0, 0
M5 """ + str(-15+dx) + """, """ + str(-15+dy) + """, """ + str(3+dz) + """, 0, 0
M5 """ + str(dx) + " , " + str(dy) + ", " + str(dz) + """, 0, 0
PAUSE 0.5

GOSUB CloseJaws
GOSUB Bolt
GOSUB OpenJaws
GOSUB DisengageGripper
PAUSE 1

M5 """ + str(-15+dx) + """, """ + str(-15+dy) + """, """ + str(3+dz) + """, 0, 0
GOSUB CloseJaws
M5 """ + str(-30+dx) + """, """ + str(-30+dy) + """, """ + str(24+dz) + """, 0, 0
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75+dz) + """, 0, 0

GOSUB OpenJawsHalf"""

def position_attach_x(dx,dy,dz):
	return """
M5 """ + str(-75) + """, """ + str(-off_camera) + """, """ + str(75) + """, 0, 120
\'\'Reload bolt and voxel
MSGBOX( Click OK to continue,64,Reload bolt and voxel!)
GOSUB EngageGripper
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75+dz) + """, 0, 120
M5 """ + str(-24+dx) + """, """ + str(-30+dy) + """, """ + str(30+dz) + """, 0, 120
M5 """ + str(-3+dx) + """, """ + str(-15+dy) + """, """ + str(15+dz) + """, 0, 120
M5 """ + str(dx) + " , " + str(dy) + ", " + str(dz) + """, 0, 120
PAUSE 0.5

GOSUB CloseJaws
GOSUB Bolt
GOSUB OpenJaws
GOSUB DisengageGripper
PAUSE 1

M5 """ + str(-3+dx) + """, """ + str(-15+dy) + """, """ + str(15+dz) + """, 0, 120
GOSUB CloseJaws
M5 """ + str(-24+dx) + """, """ + str(-30+dy) + """, """ + str(30+dz) + """, 0, 120
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75+dz) + """, 0, 120

GOSUB OpenJawsHalf"""



def position_attach_y(dx,dy,dz):
	return """
M5 """ + str(-75) + """, """ + str(-off_camera) + """, """ + str(75) + """, 0, -120
\'\'Reload bolt and voxel
MSGBOX( Click OK to continue,64,Reload bolt and voxel!)
GOSUB EngageGripper
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75+dz) + """, 0, -120
M5 """ + str(-30+dx) + """, """ + str(-24+dy) + """, """ + str(30+dz) + """, 0, -120
M5 """ + str(-15+dx) + """, """ + str(-3+dy) + """, """ + str(15+dz) + """, 0, -120
M5 """ + str(dx) + " , " + str(dy) + ", " + str(dz) + """, 0, -120
PAUSE 0.5

GOSUB CloseJaws
GOSUB Bolt
GOSUB OpenJaws
GOSUB DisengageGripper
PAUSE 1

M5 """ + str(-15+dx) + """, """ + str(-3+dy) + """, """ + str(15+dz) + """, 0, -120
GOSUB CloseJaws
M5 """ + str(-30+dx) + """, """ + str(-24+dy) + """, """ + str(30+dz) + """, 0, -120
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75+dz) + """, 0, -120

GOSUB OpenJawsHalf"""

#print position_attach_z


def attach_x(dx,dy,dz): 
	return """
M5 """ + str(-75) + """, """ + str(-off_camera) + """, """ + str(75) + """, 0, 0
\'\'\'Reload bolt
MSGBOX( Click OK to continue,64,Reload bolt!)
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75+dz) + """, 0, 120
M5 """ + str(0+dx) + """, """ + str(-75+dy) + """, """ + str(75+dz) + """, 0, 120
M5 """ + str(0+dx) + """, """+ str(-34.8109+dy) + """, """ + str(34.8109+dz) + """, 0, 120
M5 """ + str(0+dx) + """, """+ str(0+dy) + """, """ + str(0+dz) + """, 0, 120
PAUSE 0.5
GOSUB CloseJaws
GOSUB Bolt
GOSUB OpenJawsHalf
M5 """ + str(0+dx) + """, """ + str(-34.8109+dy) + """, """ + str(34.8109+dz) + """, 0, 120
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75+dz) + """, 0, 120
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75) + """, 0, 0"""


def attach_y(dx,dy,dz): 
	return """
M5 """ + str(-75) + """, """ + str(-off_camera) + """, """ + str(75) + """, 0, 0
\'\'\'Reload bolt
MSGBOX( Click OK to continue,64,Reload bolt!)
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75+dz) + """, 0, -120
M5 """ + str(-75+dx) + """, """ + str(0+dy) + """, """ + str(75+dz) + """, 0, -120
M5 """ + str(-34.8109+dx) + """, """+ str(0+dy) + """, """ + str(34.8109+dz) + """, 0, -120
M5 """ + str(0+dx) + """, """+ str(0+dy) + """, """ + str(0+dz) + """, 0, -120
PAUSE 0.5
GOSUB CloseJaws
GOSUB Bolt
GOSUB OpenJawsHalf
M5 """ + str(-75+dx) + """, """ + str(0+dy) + """, """ + str(75+dz) + """, 0, -120
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75+dz) + """, 0, -120
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75) + """, 0, -120
M5 """ + str(-75+dx) + """, """ + str(-75+dy) + """, """ + str(75) + """, 0, 0"""
