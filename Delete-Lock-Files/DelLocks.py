''' DelLocks.py
    Andrew Ortego
    aortego@esri.com
    12.14.2015

    Purpose:
        Use this script as a Python Add-In. This Add-In will delete all lock
        files in each workspace contained within an MXD's Table of Contents.
        This can be useful when user-permissions do not allow for the normal
        deletion of lock files after closing ArcMap.

    Work Flow:
        Using the closeDocument event, the Add-In will execute once the user
        closes ArcMap. Then, it scans each layer in the Table of Contents for
        it's corresponding workspace, and deletes any .lock files found in that
        workspace.

    Input:
        N/A. Set this script up as a Python Add-In, as seen here:
        www.arcgis.com/home/item.html?id=5f3aefe77f6b4f61ad3e4c62f30bff3b

    Output:
        N/A.
'''

import arcpy
import pythonaddins
import os
import glob

class DeleteLocks(object):
    """Implementation for New folder_addin.extension3 (Extension)"""
    def __init__(self):
        self.enabled = True

    def closeDocument(self):
        ''' Deletes all .lock files in each layer's directory upon closing 
            ArcMap.'''
        mxd = arcpy.mapping.MapDocument("CURRENT")
        df_list = arcpy.mapping.ListDataFrames(mxd, "*")
        for df in df_list:
            all_layers = arcpy.mapping.ListLayers(mxd, "", df)

        for layer in all_layers:
            if layer.isGroupLayer:
                pass
            else:
                file_path = arcpy.Describe(layer).path
                os.chdir(file_path)
                for lock_file in glob.glob("*.lock"):
                    os.remove(lock_file)