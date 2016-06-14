# ArcPy-Samples/Update-Definition-Query

**Demonstrates**
*  Use of a dict as an associative array, providing a visually appealing solution to replacing one query with another
*  Expressive debugging statements to inform user as to the progress of the script as it runs
*  Creation of new data to prevent unnecessary overwriting of previous data (safely run the script!)

**Usage:**

    This can be run as a standalone script in Python 2.7 with the arcpy site package installed.
    Note there are **two** versions of this script. One utilizes functions while the other just
    "gets the job done" in about 60 less lines of code. Either 
    
**Purpose:**

    Updates a subsection of a layer's Definition Query.
    The 'expressions' dictionary replaces the key with its value.
    This is useful when updating a Def. Query to reflect changes made to a feature class' properties.
    
**Work Flow:**

    Using the closeDocument event, the Add-In will execute once the user
    closes ArcMap. Then, it scans each layer in the Table of Contents for
    it's corresponding workspace, and deletes any .lock files found in that
    workspace.
    
**Input:**

    1) Update the workspace on line 22 to the directory with your MXD files.
    2) Update the "expressions" dictionary on line 24 with the old
    expression associated with the new expression. New replaces old!
    
**Output:**

    A copy of each MXD with the newly updated Definition Query.
