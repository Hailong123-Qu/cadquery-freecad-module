#File: Ex013_Locating_a_Workplane_on_a_Vertex.py
#To use this example file, you need to first follow the "Using CadQuery From Inside FreeCAD"
#instructions here: https://github.com/dcowden/cadquery#installing----using-cadquery-from-inside-freecad

#You run this example by typing the following in the FreeCAD python console, making sure to change
#the path to this example, and the name of the example appropriately.
#import sys
#sys.path.append('/home/user/Downloads/cadquery/examples/FreeCAD')
#import Ex013_Locating_a_Workplane_on_a_Vertex

#If you need to reload the part after making a change, you can use the following lines within the FreeCAD console.
#reload(Ex013_Locating_a_Workplane_on_a_Vertex)

#You'll need to delete the original shape that was created, and the new shape should be named sequentially
# (Shape001, etc).

#You can also tie these blocks of code to macros, buttons, and keybindings in FreeCAD for quicker access.
#You can get a more information on this example at
# http://parametricparts.com/docs/examples.html#an-extruded-prismatic-solid

import cadquery
import Part

#Make a basic prism
result = cadquery.Workplane("front").box(3, 2, 0.5)

#Select the lower left vertex and make a workplane
result = result.faces(">Z").vertices("<XY").workplane()

#Cut the corner out
result = result.circle(1.0).cutThruAll()

#Boiler plate code to render our solid in FreeCAD's GUI
Part.show(result.toFreecad())
