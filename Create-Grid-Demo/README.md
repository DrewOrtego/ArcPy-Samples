# Create-Grid-Demo

**Demonstrates**
* Use of ArcPy to create a polygon feature class.
* Nested for-loops and trigonometry to accurately determine the spatial extent of a feature class.
* Use of a custom class and functions.

**Usage:**

    This can be run as a standalone script in Python 2.7 with the arcpy site package installed.
    
**Purpose:**

    Creates a grid index polygon layer on top of any feature class or shapefile.
    This acts similar to the Create Index Layer geoprocessing tool available from
    ArcGIS for Desktop. This script demos how to use an array to create a feature class.
    
**Work Flow:**

    Using the closeDocument event, the Add-In will execute once the user
    closes ArcMap. Then, it scans each layer in the Table of Contents for
    it's corresponding workspace, and deletes any .lock files found in that
    workspace.
    
**Input:**

    Takes any feature class and creates a polygon feature class over it.
    (See screenshot below.)
    
**Output:**
![alt text](https://raw.githubusercontent.com/DrewOrtegoGIS/ArcPy-Samples/master/Create-Grid-Demo/output.JPG "Output")
