from os import path
from arcpy import env, mapping

env.workspace = ws = "C:\\Users\\andr7495\\Desktop"

expressions = {
    "shape_length" : "SHAPE.STLength()",
    "shape_area"   : "SHAPE.STArea()",
    "SHAPE_Length" : "SHAPE.STLength()",
    "SHAPE_Area"   : "SHAPE.STArea()",
    "SHAPE_length" : "SHAPE.STLength()",
    "SHAPE_area"   : "SHAPE.STArea()",
    }

mxds = [mapping.MapDocument(m) for m in arcpy.ListFiles("*.mxd")]

for i, mxd in enumerate(mxds):
    layers = [l for l in mapping.ListLayers(mxd) if l.isFeatureLayer and l.definitionQuery]

    for lyr in layers:
        for old_exp, new_exp in expressions.iteritems():
            if old_exp in lyr.definitionQuery:
                lyr.definitionQuery = lyr.definitionQuery.replace(old_exp, new_exp)

    mxd.saveACopy(path.join(ws, "COPY_{0}_" + mxd.filePath + ".mxd".format(i)))
    del mxd

