'''
    UpdateDefinitionQuery.py
    Andrew Ortego
    11/11/2015

    Updates a subsection of a layer's Definition Query.
    The 'expressions' dictionary replaces the key with its value.

    Input:
        1) Update the workspace on line 22 to the directory with your MXD files.
        2) Update the "expressions" dictionary on line 24 with the old
            expression associated with the new expression. New replaces old!

    Output:
        A copy of each MXD with the newly updated Definition Query.
'''

import arcpy
from arcpy import env
from os import path

env.workspace = ws = "C:\\Users\\andr7495\\Desktop"

expressions = {
    "shape_length" : "SHAPE.STLength()",
    "shape_area"   : "SHAPE.STArea()",

    "SHAPE_Length" : "SHAPE.STLength()",
    "SHAPE_Area"   : "SHAPE.STArea()",

    "SHAPE_length" : "SHAPE.STLength()",
    "SHAPE_area"   : "SHAPE.STArea()",
}

def letsGetThisPartyStarted():
    ''' For each Map Document in the workspace, check each layer for a
        definition query, and if found, update it according to the contents of
        the expression dictionary.'''
    print "Let's get this party started!\n"
    mxds = getMXDs()
    for i, mxd in enumerate(mxds):
        for layer in getLayers(mxd):
            evaluateExpression(layer)
        saveMXD(mxd, i)


def getMXDs():
    ''' Create a list of each Map Document in the workspace(s).'''
    mxds = [arcpy.mapping.MapDocument(m) for m in arcpy.ListFiles("*.mxd")]
    return mxds


def getLayers(mxd):
    ''' Collects all feature layer in a Map Document.'''
    print "{0}:\n".format(mxd.filePath)
    layers = [l for l in arcpy.mapping.ListLayers(mxd) if l.isFeatureLayer and lyr.definitionQuery]
    return layers


def evaluateExpression(lyr):
    ''' If the layer has a Definition Query, update that query using the
        dictionary of expressions.'''
    for old_exp, new_exp in expressions.iteritems():
        if old_exp in lyr.definitionQuery:
            updateExpression(lyr, old_exp, new_exp)


def updateExpression(lyr, old_exp, new_exp):
    ''' Replaces the old expression with the new one. Fill in the old/new
        associations in the "expressions" dictionary above.'''
    print "        {0}:".format(lyr.name)
    print "            Old expression: {0}".format(lyr.definitionQuery)
    lyr.definitionQuery = lyr.definitionQuery.replace(old_exp, new_exp)
    print "            New expression: {0}\n".format(lyr.definitionQuery)


def saveMXD(mxd, i):
    ''' Saves a copy of the Map Document which has had it's layers Definition
        Queries updated.'''
    file_name = "COPY_{0}_{1}".format(i, mxd.filePath)
    mxd.saveACopy(path.join(ws, file_name))
    print "    Created {0}".format(file_name)
    del mxd


if __name__ == "__main__":
    letsGetThisPartyStarted()
    print "'fin.'"

