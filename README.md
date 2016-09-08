# Shopbot-Code
Automates OpenSBP code for building voxel structures using the end effector on the 5-axis shopbot



### buildRectanglesSBP.py (formerly bruteRectanglesSBP.py)
takes in dimensions for a solid rectangular prism and the size of the seed crystal, and outputs the shopbot code for assembly. The algorithm for voxel order seems sound, and it should scale nicely. 

### shopbot_base_programs.py 
contains all of Grace and Greenfield's OpenSBP (.sbp) code for controlling the end effector in string form. It gets called by buildRectanglesSBP.py and printed out in the appropriate places.



## Visualization work

### plotCuboct.py
plots a cuboct in a 3d line graph. I'm not quite sure how to integrate it yet with buildRectanglesSBP.py

