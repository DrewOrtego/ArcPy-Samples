''' ListTransparent.py
    Andrew Ortego
    aortego@esri.com
    12.10.2015

    Purpose:
        Lists all layers in a Map Document and their corresponding transparency value.
        This is written to be ran as a Script Tool in ArcMap or ArcCatalog.

    Work Flow:
        Iterates through all layers in a Map Document's Table of Contents, excluding
        Group Layers, and lists the names of the layers found, followed by their
        transparency value.

    Input to be updated by the user:
        A single parameter, the full path of the .mxd file, is required.

    Output:
        Formatted output in the Results window of the tool.
'''

import arcpy
from arcpy import mapping as m

mxd_path = arcpy.GetParameterAsText(0)
mxd = m.MapDocument(mxd_path)

layers = [lyr for lyr in m.ListLayers(mxd) for df in m.ListDataFrames(mxd) if not lyr.isGroupLayer]

if layers:
    arcpy.AddMessage("Found the following layers and visibility values:")
    for layer in layers:
        try:
            arcpy.AddMessage("{0} -- {1}".format(layer.name, layer.transparency))
        except NameError:
            arcpy.AddMessage("{0} -- {1}".format(layer.name, "transparency not supported on layer type"))
else:
    arcpy.AddMessage("No layers found in the map document specified")

