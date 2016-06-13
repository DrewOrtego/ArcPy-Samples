''' Name:       Spatial_Describe.py

    Author:     Andrew Ortego - 08/22/2014

    Purpose:    Demonstrates an equivilency bug between 10.0 (SP0) and 10.1 -
                10.2.2. The Describe object for a feature class does not catch
                the expected spatial reference name. Instead, WGS1984 is found.
                The issue is not present for the dataset which contains the
                feature class.

    Input:      Line 16: The directory to the file geodatabase.

    Output:     Prints the spatial info for each dataset and the feature
                class(es) contained within it.
'''
geodatabase_name = "Data.gdb"

import os
try:
    import arcpy # If arcpy cannot be found, import arcgisscripting
except ImportError:
    import arcgisscripting
    arcpy = arcgisscripting.create(9.3)

arcpy.env.workspace = os.path.join(os.getcwd(), geodatabase_name) # USER INPUT

def get_data_info():
    ''' Iterates over the contents of a Geodatabase which contains datasets.'''
    print " "*4 + "Dataset Name " + str('-'*20) + " Projection --", " WKID"
    print " "*7 + "Feature Class Name " + str('-'*10) + " Projection --"," WKID"

    datasetList = arcpy.ListDatasets("*", "Feature")

    for i, dataset in enumerate(datasetList):
        print '\n' + str(i + 1) + ".",
        print_desc(dataset)
        fcList = arcpy.ListFeatureClasses("*", "", dataset)
        fcList.sort()
        for fc in fcList:
            print_desc(fc, indent=6)


def print_desc(data, width=30, indent=0):
    ''' Prints the describe object's name, spatial reference name, and the
        spatial reference's factory code.'''
    desc = arcpy.Describe(data)
    desc_sr = desc.spatialReference
    fill = str('-'*(width - len(desc.name)))
    print ' '*indent, desc.name, fill, desc_sr.name, '--', desc_sr.factoryCode


if __name__ == "__main__":
    get_data_info()

